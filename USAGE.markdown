Installation
------------

To run proxy you need Python Twisted modules (twistedmatrix.com). I do
not konw how to install them on OS X or Windows so you have to
eventually figure this out by yourself. On Linux you most likely want
to install them via distribution package manager.

Having Python and Twisted installed you can start proxy located at
bin/trf.

Running proxy
-------------

To see how to use proxy run:

        trf --help

To run proxy that multiplies download x 0.5 and uplad x 50 run:

        trf -d 0.5 -u 50

Client configuration
--------------------

You need to configure BitTorrent client to use HTTP proxy server. If
you are using Azureus for example go to:

        Tools > Options > Connection > Proxy Options

and check:

        Enable proxying of tracker communications

set host to:

        127.0.0.1

and port to (unless you specified differend port):

        7666

Extras
------

You can build RPM package using spec from misc folder. Resulting RPM
will include service file so proxy can be nicely managed by
systemd. Alternatively you can install service manually. For doing any
of those refer documentation for building RPMs and/or systemd.
