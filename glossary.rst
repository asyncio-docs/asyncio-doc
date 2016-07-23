.. _glossary:

********
Glossary
********

.. if you add new entries, keep the alphabetical sorting!

.. glossary::

    coroutine
        It's a piece of code that can be paused and resumed. Whereas threads are preemptively multitasked by the operating system, coroutines multitask cooperatively: they choose when to pause, and which coroutine to run next.

    event loop
        The event loop is the central execution device to launch execution of coroutines and handle I/O (Network, sub-processes...)

    future
        It's like a mailbox where you can subscribe to receive a result when it will be done. More details in `official documentation <https://docs.python.org/3/library/asyncio-task.html#future>`_

    task
        It represents the execution of a coroutine and take care the result in a future. More details in `official documentation <https://docs.python.org/3/library/asyncio-task.html#task>`_