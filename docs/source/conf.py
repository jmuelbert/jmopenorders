#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Spirit documentation build configuration file, created by
# sphinx-quickstart on Sun Sep 24 08:30:18 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import datetime as dt

__version__ = '0.2.0'
__short_version__ = __version__

PROJECT_NAME = 'JM OpenOrders'
PROJECT_PACKAGE_NAME = 'jmopenorders'
PROJECT_LICENSE = 'EUPL-1.2 '
PROJECT_AUTHOR = 'Jürgen Mülbert'
PROJECT_COPYRIGHT = ' 2018-{}, {}'.format(dt.datetime.now().year, PROJECT_AUTHOR)
PROJECT_URL = 'https://jmopenorders.github.io/'
PROJECT_EMAIL = 'juergen.muelbert@gmail.com'
PROJECT_LONG_DESCRIPTION = 'A BDE Tool'

PROJECT_GITHUB_USERNAME = 'jmuelbert'
PROJECT_GITHUB_REPOSITORY = 'jmopenorders'

GITHUB_PATH = '{}/{}'.format(PROJECT_GITHUB_USERNAME, PROJECT_GITHUB_REPOSITORY)
GITHUB_URL = 'https://github.com/{}'.format(GITHUB_PATH)

sys.path.insert(0, os.path.abspath('_ext'))
sys.path.insert(0, os.path.abspath('../jmopenorders'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.linkcode',
    'sphinx_autodoc_annotation',
    'edit_on_github',
    'sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = PROJECT_NAME
copyright = PROJECT_COPYRIGHT
author = PROJECT_AUTHOR

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = __short_version__
# The full version, including alpha/beta/rc tags.
release = __version__

code_branch = 'dev' if 'dev' in __version__ else 'master'

# Edit on Github config
edit_on_github_project = GITHUB_PATH
edit_on_github_branch = code_branch
edit_on_github_src_path = 'docs/source/'


def linkcode_resolve(domain, info):
    """Determine the URL corresponding to Python object."""
    if domain != 'py':
        return None
    modname = info['module']
    fullname = info['fullname']
    submod = sys.modules.get(modname)
    if submod is None:
        return None
    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except:
            return None
    try:
        fn = inspect.getsourcefile(obj)
    except:
        fn = None
    if not fn:
        return None
    try:
        source, lineno = inspect.findsource(obj)
    except:
        lineno = None
    if lineno:
        linespec = '#L%d' % (lineno + 1)
    else:
        linespec = ''
    index = fn.find('/homeassistant/')
    if index == -1:
        index = 0

    fn = fn[index:]

    return '{}/blob/{}/{}{}'.format(GITHUB_URL, code_branch, fn, linespec)

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # 'logo': 'logo.png',
    'logo_name': PROJECT_NAME,
    'description': PROJECT_LONG_DESCRIPTION,
    'github_user': PROJECT_GITHUB_USERNAME,
    'github_repo': PROJECT_GITHUB_REPOSITORY,
    'github_type': 'star',
    'github_banner': True,
    'travis_button': True,
    # 'touch_icon': 'logo-apple.png',
    # 'fixed_sidebar': True, # Re-enable when we have more content
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = 'Home-Assistant v0.27.0'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = '_static/logo.png'

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.
# This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
# html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        # 'links.html',
        'navigation.html',
        # 'sourcelink.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
html_use_smartypants = True

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'jmbdedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'jmopenorders.tex', 'jmopenorders Documentation',
     'Jürgen Mülbert', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'jmopenorders.tex', 'jmopenorders Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'jmopenorders.tex', 'jmopenorders Documentation',
     author, 'jmopenorders', 'One line description of project.',
     'Miscellaneous'),
]
