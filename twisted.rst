++++++++++++++++++++++++++++++++++++++
Learn asyncio if you come from Twisted
++++++++++++++++++++++++++++++++++++++

The `Twisted project <https://twistedmatrix.com/trac/>`_ is probably one of the
oldest libraries that supports asynchronous programming in Python.
It has been used by many programmers to develop a variety of applications.
It supports many network protocols and can be used for many different
types of network programming.
In fact, asyncio was heavily inspired by Twisted.
The expertise of several Twisted developers had been incorporated in
asyncio.
Soon, there will be a version of Twisted that is based on asyncio.



Rosetta Stone
=============

This tables shows equivalent concepts in Twisted and asyncio.

========================  ==================================
Twisted                   asyncio
========================  ==================================
``Deferred``              ``asyncio.Future``
``deferToThread(func)``   ``loop.run_in_executor(None, func)``
``@inlineCallbacks``      ``async def``
``reactor.run()``         ``loop.run_forever()``
========================  ==================================


Deferred example
================

This small example shows two equivalent programs, one implemented in Twisted
and one in asyncio.

+--------------------------------------------------+--------------------------------------------------+
| Twisted                                          | asyncio                                          |
+==================================================+==================================================+
| Basic Twisted example using deferred:            | Similar example written using asyncio:           |
|                                                  |                                                  |
| .. literalinclude:: examples/twisted_deferred.py | .. literalinclude:: examples/asyncio_deferred.py |
+--------------------------------------------------+--------------------------------------------------+

