Hello Clock
^^^^^^^^^^^

Example illustrating how to schedule two coroutines to run concurrently.
They run for ten minutes, during which the first coroutine is scheduled every
second, while the second is scheduled every minute.

The function `asyncio.gather` is used to schedule both coroutines at once.

.. literalinclude:: hello_clock.py
