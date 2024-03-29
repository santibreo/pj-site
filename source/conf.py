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
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'PJnotes'
copyright = '2021, Prophet Jeremy'
author = 'Prophet Jeremy'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx_pj_theme"
]

# Avoid section label collisions
autosectionlabel_prefix_document = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "paraiso-dark"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# List of roles that I add to Sphinx for a better documentation
rst_prolog = """
.. role:: underline
   :class: underline-text

.. role:: strikethrough
   :class: strikethrough-text

.. role:: highlight
   :class: highlight-text-yellow

.. role:: highlight-purple
   :class: highlight-text-purple

.. role:: highlight-blue
   :class: highlight-text-blue

.. role:: highlight-red
   :class: highlight-text-red

.. role:: highlight-green
   :class: highlight-text-green
"""

rst_epilog = """
.. _Python: https://python.org
.. _Git: https://git-scm.com/
.. _Flask: https://flask.palletsprojects.com/en/latest/
.. _Gogs: https://gogs.io/
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme_path = [
    "../../sphinx_pj_theme"
]
html_css_files = [
    'css/fontawesome-all.css',
]
html_theme = 'sphinx_pj_theme'
html_permalinks = True
html_permalinks_icon = '&sect;'
#  html_favicon = "_static/favicon.ico"
html_copy_source = False
html_show_source_link = False
html_codeblock_linenos_style = 'table'
html_sidebars = {
    'cv*': ['sb_cv.html', 'sb_socialicons.html'],
    '**': ['sb_navigation.html', 'sb_toc.html', 'sb_searchbox.html', 'sb_socialicons.html'],
    'index': ['sb_searchbox.html', 'sb_socialicons.html'],
    'search': [],
    'about': [],
    'recommendations': [],
}

html_theme_options = {
    "owner": author,
    "contact_email": "santibreo@gmail.com",
    "social_urls": {
        "github": "https://github.com/santibreo",
        "x-twitter": "https://twitter.com/santibreo",
        "linkedin": "https://www.linkedin.com/in/santibreo/",
    },
    "main_language": 'english',
    "cv_url": "https://santibreo.github.io/pj-site/cv.html",
    "cv_name": "Santiago Breogán",
    "cv_surname": "Pérez Pita",
    "cv_profile_pic": "",
    "cv_phone": "600 395 845",
    "cv_location": "Madrid",
    # After this, fields that are language dependent
    "cv_job_position": {
        'english': "Data scientist",
        'spanish': "Científico de datos",
    },
    "cv_main_info": {
        'english': {
            "languages": {
                "english": 8,
                "spanish": 10,
            },
            "Useful info": {
                "birthdate": "25 July 1992",
                "driving-license": "B2"
            }
        },
        'spanish': {
            "idiomas": {
                "inglés": 8,
                "castellano": 10,
            },
            "Info. útil": {
                "nacimiento": "25 de Julio, 1992",
                "permiso de conducir": "B2"
            }
        }
    },
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
