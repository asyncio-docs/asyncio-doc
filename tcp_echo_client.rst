TCP echo client protocol
------------------------

TCP echo client  using the :meth:`BaseEventLoop.create_connection` method, send
data and wait until the connection is closed:

.. literalinclude:: examples/tcp_echo_client.py


The event loop is running twice. The
:meth:`~BaseEventLoop.run_until_complete` method is preferred in this short
example to raise an exception if the server is not listening, instead of
having to write a short coroutine to handle the exception and stop the
running loop. At :meth:`~BaseEventLoop.run_until_complete` exit, the loop is
no longer running, so there is no need to stop the loop in case of an error.
