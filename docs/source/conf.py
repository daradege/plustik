import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'autoapi.extension',
    'sphinx_copybutton',
    'sphinx_design',
]

autoapi_dirs = ['../../plustik']
autoapi_type = 'python'
autoapi_root = 'api'
autoapi_options = [
    'members',
    'undoc-members',
    'show-inheritance',
    'show-module-summary',
    'special-members',
]

autoapi_add_toctree_entry = True
autoapi_keep_files = False

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

project = 'Plustik'
copyright = '2026, Plustik Team'
author = 'Plustik Team'

html_theme = 'furo'
html_title = 'Plustik Documentation'

html_theme_options = {
    "top_of_page_button": "arrow",
    "source_repository": "https://github.com/daradege/plustik",
    "source_branch": "main",
    "source_directory": "docs/source/",
    "navigation_with_keys": True,
    "announcement": "<strong>🚀 Plustik Beta!</strong>",
}

html_static_path = ['_static']
html_show_sourcelink = False

autodoc_typehints = 'description'
autodoc_member_order = 'bysource'

exclude_patterns = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
