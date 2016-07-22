+++++++++++++++++
Producer/consumer
+++++++++++++++++

Simple example
==============

A simple producer/consumer example, using an `asyncio.Queue
<http://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue>`_:

.. literalinclude:: examples/producer_consumer.py


Using task_done()
=================


A simple producer/consumer example, using `Queue.task_done
<http://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.task_done>`_
and `Queue.join
<http://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.join>`_:

.. literalinclude:: examples/producer_consumer_2.py

For more information, see the `asyncio queue documentation
<http://docs.python.org/3/library/asyncio-queue.html>`_.
