#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# The A+ settings in this file are documented in
# https://github.com/apluslms/a-plus-rst-tools/blob/master/README.md

import sys
import os


# -- Aplus configuration --------------------------------------------------
course_open_date = '2020-07-01'
course_close_date = '2030-12-31'
questionnaire_default_submissions = 5
program_default_submissions = 10
default_max_group_size = 1
use_wide_column = False
static_host = os.environ.get('STATIC_CONTENT_HOST', 'http://localhost:8080/static/default')

# Define the base URL of the ACOS exercises if the default value is incorrect.
# The internal IP address of the ACOS container should be used in local testing
# and in production, the URL of the ACOS production server.
on_container = static_host and '8080' in static_host
if on_container:
    acos_submit_base_url = 'http://acos:3000'
else:
    acos_submit_base_url = 'https://acos.cs.aalto.fi'

override = {
    'jututfeedback': {
        'url': ('http://jutut:8082/feedback/testcoursemultilang/{key}' if on_container
                else 'https://jutut.minus.cs.aalto.fi/feedback/testcoursemultilang/{key}'),
        'max_points': 2,
        'points_to_pass': 1,
    },
}
# The JavaScript code used by the enrollment questionnaire is hosted in the course repo,
# so we need to know the course key in order to craft the URL of the JS.
# This RST substitution is used to insert the script in the questionnaire RST code.
course_key = os.environ.get('COURSE_KEY', 'default')
rst_prolog = '''.. |enroll-js-script| raw:: html

  <script src="{static_host}/_static/enrollmentquiz.js"></script>
'''.format(static_host=static_host)

rst_prolog += '''
.. role:: glyphicon-info-sign
  :class: glyphicon glyphicon-info-sign
.. role:: raw-html(raw)
   :format: html
.. role:: glyphicon-pencil
  :class: glyphicon glyphicon-pencil
.. role:: glyphicon-certificate
  :class: glyphicon glyphicon-certificate
.. role:: glyphicon-console
  :class: glyphicon glyphicon-console
.. role:: important
  :class: important
'''

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

sys.path.append(os.path.abspath('a-plus-rst-tools'))
sys.path.append(os.path.abspath('a-plus-rst-tools/directives'))

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'aplus_setup',
    'media',
    'point_of_interest',
    'row',
    'tabs',
    'annotated',
    'thebe',
]

include_tab_js = True
include_tab_css = True
include_annotated_js = True
include_annotated_css = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Aplus manual'
copyright = '2021, Aalto University'
author = 'NN'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y.Z version.
version = '0.1.1'
# The full version, including alpha/beta/rc tags.
release = '0.1.1-beta'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'exercises/solutions', '_data', 'enrollment']

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# A+ requires the aplus theme, which is defined in a-plus-rst-tools.
html_theme = 'aplus'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'use_wide_column': use_wide_column,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['a-plus-rst-tools/theme']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Disable automatic quote and dash conversions.
smartquotes = False
