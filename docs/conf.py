# -*- coding: utf-8 -*-
#
# SPDX-FileCopyrightText: 2019-2021 Project jmopenorders, Jürgen Mülbert
#
# SPDX-License-Identifier: EUPL-1.2
#

"""Sphinx configuration."""
from datetime import datetime

project = "jmopenorders"
author = "Jürgen Mülbert"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "sphinx_rtd_theme",
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
