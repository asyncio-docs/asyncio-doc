Hello World with call_soon()
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Example using the :meth:`BaseEventLoop.call_soon` method to schedule a
callback. The callback displays ``"Hello World"`` and then stops the event
loop::

    import asyncio

    def hello_world(loop):
        print('Hello World')
        loop.stop()

    loop = asyncio.get_event_loop()

    # Schedule a call to hello_world()
    loop.call_soon(hello_world, loop)

    # Blocking call interrupted by loop.stop()
    loop.run_forever()
    loop.close()
