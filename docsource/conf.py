# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import shlex
import sphinx_rtd_theme
import recommonmark
from recommonmark.transform import AutoStructify

import recommonmark
from recommonmark.parser import CommonMarkParser


# -- Project information -----------------------------------------------------

project = 'Qubinode'
copyright = '2021, Toshin, Rodrique, Joey, Abner'
author = 'Toshin, Rodrique, Joey, Abner'

# The full version, including alpha/beta/rc tags
release = '2.5'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'recommonmark',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
master_doc = 'index'
source_suffix = [".rst"]
project = u'Qubinode'
author = u'Oluwatosin Akinosho, Rodrique Heron, Joey Amanchukwu, Abnerson Malivert'
         
release = '2.4.5'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
#exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#html_theme_path = [sphinx_rtd_theme]
html_theme_options = {
    #'display_version': False,
    #'navigation_depth': 2,
    #'logo_only': True,
}

html_logo='QubinodeFinal.png'
html_favicon='icon.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

source_parsers = {
   '.md': CommonMarkParser,
}

def setup(app):
   app.add_config_value('recommonmark_config', {
       'enable_eval_rst': True,
   }, True)
   app.add_transform(AutoStructify)