import logging
from pprint import pprint as pp
import socket
import sys

import click
from pysensu.api import SensuAPI
"""
  A cli wrapper around some of the Sensu ReST API. Use `--help` for cli invocation or `make html` for Sphinx doc.

  .. moduleauthor:: Duncan Hutty (dhutty) <dhutty@allgoodbits.org>
"""

LOG_LEVELS = ['ERROR', 'INFO', 'DEBUG']
pass_api = click.make_pass_decorator(SensuAPI)
logger = logging.getLogger(__name__)


@click.group()
@click.option('-l', '--log-level', default='INFO', type=click.Choice(LOG_LEVELS), help='Specify log verbosity.')
@click.option('-u', '--username', help='Sensu username.')
@click.option('-p', '--password', help='Sensu password.')
@click.option(
    '--scheme', default='http', type=click.Choice(['http', 'https']), help='Specify protocol', show_default=True)
@click.option('--server', default='localhost', help='Specify the Sensu server', show_default=True)
@click.option('--port', default=4567, type=int, help='Specify the Sensu port', show_default=True)
@click.pass_context
def cli(ctx, log_level, scheme, server, port, username=None, password=None):
    # Create a SensuAPI object and remember it as as the context object.  From
    # this point onwards other commands can refer to it by using the
    # @pass_api decorator.
    ctx.obj = SensuAPI('{}://{}:{}'.format(scheme, server, port), username=username, password=password)
    logging.basicConfig(level=log_level)


@cli.command('subs', short_help="Show info on subscriptions")
@click.option(
    '--host', default=socket.gethostname(), help='Specify sensu target client', show_default=True, multiple=True)
@pass_api
def subs(api, host):
    pp(api.get_subscriptions(host))


@cli.command('silenced', short_help="List Silences")
@click.option('--limit', type=int, help='The number of silences to return. Default, unlimited.')
@click.option('--offset', type=int, help='The number of silences to offset efore returning silences. Requires --limit.')
@pass_api
def silenced(api, limit, offset):
    pp(api.get_silenced(limit=limit, offset=offset))


@cli.command('silence', short_help="Create Silence")
@click.option(
    '--host', default=[socket.getfqdn()], help='Specify sensu target client(s)', show_default=True, multiple=True)
@click.option('--check', help='The check to silence. required, unless subscription is specified')
@click.option('--subscription', help='The subscription to silence. required, unless check is specified')
@click.option('--expire', type=int, help='The expiry time, in seconds, for the new Silence.')
@click.option('--reason', help='Explanatory detail.')
@click.option('--creator', help='Explanatory detail.')
@pass_api
def silence(api, **kwargs):
    api.post_silence_request(kwargs)


@cli.command('unsilence', short_help="Clear silencing")
@click.option(
    '--host', default=[socket.getfqdn()], help='Specify sensu target client(s)', show_default=True, multiple=True)
@click.option('--check', help='The check to silence. Required, unless subscription is specified')
@click.option(
    '--id',
    type=int,
    help='The id (intersection of subscription and check) of the subscription to clear the silence entry for.')
@click.option('--subscription', help='The subscription to silence. Required, unless check is specified')
@pass_api
def unsilence(api, **kwargs):
    api.clear_silence(kwargs)


@cli.command('info', short_help="Show info about the Sensu API")
@pass_api
def info(api):
    pp(api.get_info())


if __name__ == '__main__':
    sys.exit(cli())
