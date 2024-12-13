# -*- coding: utf-8 -*-
"""Nox sessions configuration file.

Defines reusable Nox sessions for tasks like linting, testing, type checking,
and documentation building.
"""
import hashlib
import shutil
import sys
from pathlib import Path
from textwrap import dedent

import nox
from nox.sessions import Session

# Project-specific configurations
package = "test"
python_versions = ["3.9", "3.10", "3.11", "3.12"]  # Define supported Python versions
nox.options.sessions = (
    "pre-commit",
    "safety",
    "ruff",
    "tests",
    "typeguard",
    "docs-build",
)

class Poetry:
    """Helper class for invoking Poetry inside a Nox session."""

    def __init__(self, session: Session) -> None:
        """Initialize with a Nox session."""
        self.session = session

    def export(self, path: Path, *, dev: bool) -> None:
        """Export dependencies to a requirements file."""
        options = ["--dev"] if dev else []
        self.session.run(
            "poetry",
            "export",
            "--format=requirements.txt",
            f"--output={path}",
            *options,
            external=True,
        )

    def build(self, *args: str) -> str:
        """Build the package and return the wheel filename."""
        output = self.session.run(
            "poetry", "build", *args, external=True, silent=True, stderr=None
        )
        assert isinstance(output, str)  # Ensure output is a string
        return output.split()[-1]  # Extract the wheel filename

def export_requirements(session: Session, *, dev: bool) -> Path:
    """Export Poetry lock file to a requirements file with caching."""
    tmpdir = Path(session.create_tmp())
    name = "dev-requirements.txt" if dev else "requirements.txt"
    path = tmpdir / name
    hashfile = tmpdir / f"{name}.hash"

    lockdata = Path("poetry.lock").read_bytes()
    digest = hashlib.blake2b(lockdata).hexdigest()

    if not hashfile.is_file() or hashfile.read_text() != digest:
        Poetry(session).export(path, dev=dev)
        hashfile.write_text(digest)

    return path

def install_package(session: Session) -> None:
    """Build and install the package along with its dependencies."""
    poetry = Poetry(session)
    wheel = poetry.build("--format=wheel")
    requirements = export_requirements(session, dev=False)

    session.install(f"--requirement={requirements}")
    session.install("--no-deps", "--force-reinstall", f"dist/{wheel}")

def install(session: Session, *args: str) -> None:
    """Install development dependencies in the session's virtual environment."""
    requirements = export_requirements(session, dev=True)
    session.install(f"--constraint={requirements}", *args)

def activate_virtualenv_in_precommit_hooks(session: Session) -> None:
    """Patch pre-commit hooks to use the session's virtual environment."""
    if session.bin is None or session.env.get("VIRTUAL_ENV") is None:
        return

    virtualenv = session.env["VIRTUAL_ENV"]
    hookdir = Path(".git") / "hooks"
    if not hookdir.is_dir():
        return

    for hook in hookdir.iterdir():
        if hook.name.endswith(".sample") or not hook.is_file():
            continue

        text = hook.read_text()
        bindir = repr(session.bin)[1:-1]  # Strip quotes
        if bindir in text or bindir.lower() in text.lower():
            lines = text.splitlines()
            if lines[0].startswith("#!") and "python" in lines[0].lower():
                header = dedent(
                    f"""\
                    import os
                    os.environ["VIRTUAL_ENV"] = {virtualenv!r}
                    os.environ["PATH"] = os.pathsep.join((
                        {session.bin!r},
                        os.environ.get("PATH", ""),
                    ))
                    """
                )
                lines.insert(1, header)
                hook.write_text("\n".join(lines))

@nox.session(name="pre-commit", python="3.9")
def precommit(session: Session) -> None:
    """Run linting using pre-commit."""
    args = session.posargs or ["run", "--all-files", "--show-diff-on-failure"]
    install(
        session,
        "ruff",
        "pre-commit",
        "pre-commit-hooks",
        "reorder-python-imports",
    )
    session.run("pre-commit", *args)
    if args and args[0] == "install":
        activate_virtualenv_in_precommit_hooks(session)

@nox.session(python="3.9")
def safety(session: Session) -> None:
    """Scan dependencies for vulnerabilities."""
    install(session, "safety")
    requirements = export_requirements(session, dev=True)
    session.run("safety", "check", f"--file={requirements}", "--bare")

@nox.session(python=python_versions)
def ruff(session: Session) -> None:
    """Run linting with Ruff."""
    args = session.posargs or ["."]
    install_package(session)
    install(session, "ruff")
    session.run("ruff", "check", *args)

@nox.session(python=python_versions)
def tests(session: Session) -> None:
    """Run the test suite with coverage reporting."""
    install_package(session)
    install(session, "coverage[toml]", "pytest", "faker", "openpyxl")
    try:
        session.run("coverage", "run", "--parallel", "-m", "pytest", *session.posargs)
    finally:
        session.notify("coverage")

@nox.session
def coverage(session: Session) -> None:
    """Generate a coverage report."""
    has_args = session.posargs and len(session._runner.manifest) == 1
    args = session.posargs if has_args else ["report"]

    install(session, "coverage[toml]")

    if not has_args and any(Path().glob(".coverage.*")):
        session.run("coverage", "combine")

    session.run("coverage", *args)

@nox.session(python=python_versions)
def typeguard(session: Session) -> None:
    """Perform runtime type checking with Typeguard."""
    install_package(session)
    install(session, "pytest", "typeguard", "faker", "openpyxl")
    session.run("pytest", f"--typeguard-packages={package}", *session.posargs)

@nox.session(python=python_versions)
def xdoctest(session: Session) -> None:
    """Run examples using xdoctest."""
    args = session.posargs or ["all"]
    install_package(session)
    install(session, "xdoctest")
    session.run("python", "-m", "xdoctest", package, *args)

@nox.session(name="docs-build", python="3.9")
def docs_build(session: Session) -> None:
    """Build the project documentation."""
    args = session.posargs or ["docs", "docs/_build"]
    install_package(session)
    install(session, "sphinx")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run("sphinx-build", *args)

@nox.session(python="3.9")
def docs(session: Session) -> None:
    """Build and serve documentation with live reloading."""
    args = session.posargs or ["--open-browser", "docs", "docs/_build"]
    install_package(session)
    install(session, "sphinx", "sphinx-autobuild")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run("sphinx-autobuild", *args)
