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
@inlineCallbacks          @coroutine
reactor.run()             loop.run_forever()
========================  ==================================
