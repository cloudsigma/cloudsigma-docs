# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys, os

EXAMPLE_SNIPPETS_DUMP_PATH = os.getenv('EXAMPLE_SNIPPETS_DUMP_PATH', '~/.turlo/dumps/')

if os.path.exists(os.path.expanduser(EXAMPLE_SNIPPETS_DUMP_PATH)) and not os.path.exists(os.path.join(os.path.dirname(__file__), 'dumps')):
    os.symlink(os.path.expanduser(EXAMPLE_SNIPPETS_DUMP_PATH), os.path.join(os.path.dirname(__file__), 'dumps'))
sys.path.append(os.path.abspath('exts'))

extensions = ['sphinxcontrib.httpdomain', 'sphinx.ext.viewcode', 'sphinxcontrib.programoutput', 'include_json']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'CloudSigma API'

copyright = u'2024, CloudSigma'

version = '2.0'
release = 'v2'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_last_updated_fmt = '%b %d, %Y'

html_show_sphinx = False

htmlhelp_basename = 'CloudSigmaAPIver20doc'

latex_elements = {}

latex_documents = [
  ('index', 'CloudSigmaAPIver20.tex', u'CloudSigma API ver. 2.0 Documentation',
   u'CloudSigma', 'manual'),
]

man_pages = [
    ('index', 'cloudsigmaapiver20', u'CloudSigma API ver. 2.0 Documentation',
     [u'CloudSigma'], 1)
]

texinfo_documents = [
  ('index', 'CloudSigmaAPIver20', u'CloudSigma API ver. 2.0 Documentation',
   u'CloudSigma', 'CloudSigmaAPIver20', 'One line description of project.',
   'Miscellaneous'),
]

html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'green',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
