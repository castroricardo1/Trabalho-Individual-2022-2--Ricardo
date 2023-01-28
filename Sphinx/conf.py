import os
import sys
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Trabalho gces'
copyright = '2023, Ricardo Loureiro'
author = 'Ricardo Loureiro'
release = '2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

sys.path.append("/home/me/docproj/ext/breathe/")
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosectionlabel', 'breathe', 'sphinx.ext.autosummary', 'sphinx.ext.coverage', 'sphinx.ext.doctest', 'sphinx.ext.duration', 'sphinx.ext.extlinks', 'sphinx.ext.githubpages', 'sphinx.ext.graphviz', 'sphinx.ext.ifconfig', 'sphinx.ext.imgconverter', 'sphinx.ext.inheritance_diagram', 'sphinx.ext.intersphinx', 'sphinx.ext.todo', 'sphinx.ext.viewcode' ]
breathe_projects = {"myproject": "/documentation/xml"}
breathe_default_project = "myproject"


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'pt'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
