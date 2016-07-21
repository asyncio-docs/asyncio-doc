TCP echo client protocol
------------------------

TCP echo client  using the :meth:`BaseEventLoop.create_connection` method, send
data and wait until the connection is closed::

    import asyncio

    class EchoClientProtocol(asyncio.Protocol):
        def __init__(self, message, loop):
            self.message = message
            self.loop = loop

        def connection_made(self, transport):
            transport.write(self.message.encode())
            print('Data sent: {!r}'.format(self.message))

        def data_received(self, data):
            print('Data received: {!r}'.format(data.decode()))

        def connection_lost(self, exc):
            print('The server closed the connection')
            print('Stop the event loop')
            self.loop.stop()

    loop = asyncio.get_event_loop()
    message = 'Hello World!'
    coro = loop.create_connection(lambda: EchoClientProtocol(message, loop),
                                  '127.0.0.1', 8888)
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()

The event loop is running twice. The
:meth:`~BaseEventLoop.run_until_complete` method is preferred in this short
example to raise an exception if the server is not listening, instead of
having to write a short coroutine to handle the exception and stop the
running loop. At :meth:`~BaseEventLoop.run_until_complete` exit, the loop is
no longer running, so there is no need to stop the loop in case of an error.
