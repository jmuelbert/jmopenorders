# -*- coding: utf-8 -*-
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
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "sphinx_rtd_theme",
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
