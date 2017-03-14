sensu-cli
=========

version number: 0.1.0
author: Duncan Hutty

Overview
--------

A convenient CLI for some of the [Sensu REST API].

[Sensu REST API]: https://sensuapp.org/docs/0.28/api/

Installation
------------

To install use pip:

    $ pip install sensu-cli

Or clone the repo:

    $ git clone https://github.com/dhutty/sensu-cli.git
    $ python setup.py install

Usage
-----

See the built-in help:

    $ sensu --help
    Usage: sensu [OPTIONS] COMMAND [ARGS]...

    Options:
      -l, --log-level [ERROR|INFO|DEBUG]
                                      Specify log verbosity.
      -u, --username TEXT             Sensu username.
      -p, --password TEXT             Sensu password.
      --scheme [http|https]           Specify protocol  [default: http]
      --server TEXT                   Specify the Sensu server  [default:
                                      localhost]
      --port INTEGER                  Specify the Sensu port  [default: 4567]
      --help                          Show this message and exit.

    Commands:
      info       Show info about the Sensu API
      silence    Create Silence
      silenced   List Silences
      subs       Show info on subscriptions
      unsilence  Clear silencing
