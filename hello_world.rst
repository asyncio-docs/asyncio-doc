Hello World
^^^^^^^^^^^

This is a series of examples showing the basics of how write coroutines and
schedule them in the asyncio event loop.

1. Simple coroutine

Example using the :meth:`BaseEventLoop.run_until_complete` method to schedule
simple function that will wait one second, print 'hello' and then finish.

Because it is launched with `run_until_complete`, the event loop itself
with terminate once the coroutine is completed.

.. literalinclude:: examples/hello_world.py

2. Creating tasks

This second example show how you can schedule multiple coroutines in the
event loop, and then run the event loop.

Notice that this example will print 'second_hello' before 'first_hello',
as the second task scheduled waits longer that the first one before printing.

Also note that this example will never terminate, as the loop is asked to
`run_forever`.

.. literalinclude:: examples/create_task.py

3. Stopping the loop

This third example adds another task that will stop the event loop before
all scheduled tasks could execute, which results in a warning.

.. literalinclude:: examples/stop_loop.py

| Task was destroyed but it is pending!
| task: <Task pending coro=<say() done, defined at examples/loop_stop.py:3> wait_for=<Future pending cb=[Task._wakeup()]>>
