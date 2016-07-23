Hello Clock
^^^^^^^^^^^

Example illustrating how to schedule two :term:`coroutines <coroutine>` to run concurrently.
They run for ten minutes, during which the first :term:`coroutine <coroutine>` is scheduled every
second, while the second is scheduled every minute.

The function `asyncio.gather` is used to schedule both :term:`coroutines <coroutine>` at once.

.. literalinclude:: examples/hello_clock.py
