.. _sock:

Socket Programing
=================

Sockets are the endpoints of a bidirectional communications channel.
Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.

1. A Simple Server
--------------------------

.. literalinclude:: server.py
   :emphasize-lines: 5,6,17,21


2. A Simple Client
--------------------------

.. literalinclude:: client.py
   :emphasize-lines: 5,6,17

Command: ::

    # Following would start a server in background.
    $ python server.py &

    # Once server is started run client as follows:
    $ python client.py

    Output:
    on server terminal
    Got a connection from ('192.168.1.10', 3747)
    On client terminal
    Thank you for connecting