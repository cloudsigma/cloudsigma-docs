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

copyright = u'2023, CloudSigma'

version = '2.0'
release = 'v2'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'default'

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
