#
# SPDX-FilecopyrightText: 2019-2021 PROJECT jmopenorders, Jürgen Mülbert
#
# SPDX-License-Identifier: EUPL-1.2
#
"""Sphinx configuration."""
from datetime import datetime

PROJECT = "jmopenorders"
AUTHOR = "Jürgen Mülbert"
COPYRIGHT = f"{datetime.now().year}, {AUTHOR}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_click"]
AUTODOC_TYPEHINTS = "description"
HTML_THEME = "furo"
