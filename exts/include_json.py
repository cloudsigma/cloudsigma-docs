__author__ = 'islavov'

import logging

import codecs

from docutils.parsers.rst import Directive, directives
from docutils import nodes

from sphinx.util import parselinenos
from sphinx.util.nodes import set_source_info
import json


LOG = logging.getLogger(__name__)

class IncludeJson(Directive):
    """
    Like ``.. include:: :literal:``, but only warns if the include file is
    not found, and does not raise errors.  Also has several options for
    selecting what to include.
    """

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'hide_header': directives.unchanged_required,
        'hide_body': directives.unchanged_required,
        'keys': directives.unchanged_required,
        'accessor': directives.unchanged_required,
        'linenos': directives.flag,
        'tab-width': int,
        'encoding': directives.encoding,
        'prepend': directives.unchanged_required,
        'append': directives.unchanged_required,
    }

    def run(self):
        document = self.state.document
        if not document.settings.file_insertion_enabled:
            return [document.reporter.warning('File insertion disabled',
                                              line=self.lineno)]
        env = document.settings.env
        rel_filename, filename = env.relfn2path(self.arguments[0])

        LOG.debug('rel_filenane = %r, filename = %r', rel_filename, filename)
        encoding = self.options.get('encoding', env.config.source_encoding)
        codec_info = codecs.lookup(encoding)
        try:
            f = codecs.StreamReaderWriter(open(filename, 'rb'),
                    codec_info[2], codec_info[3], 'strict')
            file_contents= f.read()
            f.close()
        except (IOError, OSError):
            return [document.reporter.warning(
                'Include file %r not found or reading it failed' % filename,
                line=self.lineno)]
        except UnicodeError:
            return [document.reporter.warning(
                'Encoding %r used for reading included file %r seems to '
                'be wrong, try giving an :encoding: option' %
                (encoding, filename))]

        fcont = file_contents.split('\n\n', 1)
        if len(fcont) == 2:
            header, body = fcont
        else:
            header = ""
            body = file_contents

        accessor = self.options.get('accessor')
        keys = self.options.get('keys')
        if accessor or keys:
            try:
                traversed = json.loads(body)
            except:
                return [document.reporter.warning(
                    'Include file %r does not contain valid json' % filename, line=self.lineno)]

            try:
                if accessor:
                    for acc in accessor.split('.'):
                        if isinstance(traversed, dict):
                            traversed = traversed[acc]
                        else:
                            traversed = traversed[int(acc)]

                if isinstance(traversed, dict) and keys is not None:
                    res = {}
                    for key in keys.split(','):
                        res[key] = traversed[key]
                else:
                    res = traversed

                body = json.dumps(res, sort_keys=True, indent=4)
            except Exception as exc:
                LOG.exception('Error processing %r', filename)
                return [
                    document.reporter.warning(
                        'Error processing {}: {!r}'.format(filename, exc),
                        line=self.lineno
                    )
                ]


        text=""
        if not self.options.get('hide_header'):
            text +="%s\n\n" % header

        if not self.options.get('hide_body'):
            text += body

        prepend = self.options.get('prepend')
        append = self.options.get('append')
        if prepend:
            text = prepend + '\n' + text
        if append:
            text += append + '\n'

        if self.options.get('tab-width'):
            text = text.expandtabs(self.options['tab-width'])
        retnode = nodes.literal_block(text, text, source=filename)
        set_source_info(self, retnode)
        retnode['language'] = 'javascript'
        if 'linenos' in self.options:
            retnode['linenos'] = True

        env.note_dependency(rel_filename)
        return [retnode]


def setup(app):
    app.require_sphinx('1.0')
    app.add_directive('includejson', IncludeJson)
