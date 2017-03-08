import sys

import click

"""
  A cli wrapper around some of the Sensu ReST API. Use `--help` for cli invocation or `make html` for Sphinx doc.

  .. moduleauthor:: Duncan Hutty (dhutty) <dhutty@allgoodbits.org>
"""

LOG_LEVELS = ['ERROR', 'INFO', 'DEBUG']


@click.group()
@click.option('-l', '--log-level', default='INFO', type=click.Choice(LOG_LEVELS), help='Specify log verbosity.')
@click.pass_context
def cli(ctx, log_level):
    pass

if __name__ == '__main__':
    sys.exit(cli())
