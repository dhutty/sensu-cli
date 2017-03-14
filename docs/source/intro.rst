=====================
Introducing sensu-cli
=====================

`sensu-cli`_ is a convenient CLI wrapper around some of the `Sensu ReST API`_. The original 'itch' was to create a tool
for sysadmins to use to silence Sensu alerts when administering hosts/services.

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


.. _`sensu-cli`: https://github.com/dhutty/sensu-cli
.. _`Sensu ReST API`: https://sensuapp.org/docs/0.28/api/
