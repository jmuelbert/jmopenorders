# -*- coding: utf-8 -*-
"""Sphinx configuration."""
from datetime import datetime


project = "jmopenorders"
author = "Jürgen Mülbert"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
autodoc_typehints = "description"
