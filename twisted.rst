++++++++++++++++++++++++++++++++++++++
Learn asyncio if you come from Twisted
++++++++++++++++++++++++++++++++++++++

`Twisted project <https://twistedmatrix.com/trac/>`_.


Rosetta Stone
=============

========================  ==================================
Twisted                   asyncio
========================  ==================================
Deferred                  asyncio.Future
deferToThread(func)       loop.run_in_executor(None, func)
@inlineCallbacks          async def
reactor.run()             loop.run_forever()
========================  ==================================


Deferred example
================

+--------------------------------------------------+--------------------------------------------------+
| Twisted                                          | asyncio                                          |
+==================================================+==================================================+
| Basic Twisted example using deferred:            | Similar example written using asyncio:           |
|                                                  |                                                  |
| .. literalinclude:: examples/twisted_deferred.py | .. literalinclude:: examples/asyncio_deferred.py |
+--------------------------------------------------+--------------------------------------------------+

