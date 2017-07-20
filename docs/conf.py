#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# General information about the project.
project = 'TestName'
copyright = '2016-2017, ale5000'
author = 'ale5000'

# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
]

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'pycompatlayer')))
