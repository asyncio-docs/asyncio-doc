+++++++++++++++++++
asyncio performance
+++++++++++++++++++

Random notes about tuning asyncio for performance. Performance means two
different terms which might be incompatible:

* Number of concurrent requests per second
* Request latency in seconds: min/average/max time to complete a request


Architecture: Worker processes
==============================

Because of its GIL, CPython is basically only able to use 1 CPU. To increase
the number of concurrent requests, one solution is to spawn multiple worker
processes. See for example:

* `Gunicorn <http://docs.gunicorn.org/en/stable/design.html>`_
* `API-Hour <http://pythonhosted.org/api_hour/>`_


Stream limits
=============

* `limit parameter of StreamReader/open_connection()
  <https://docs.python.org/dev/library/asyncio-stream.html#streamreader>`_
* `set_write_buffer_limits() low/high water mark on writing for transports
  <https://docs.python.org/dev/library/asyncio-protocol.html#asyncio.WriteTransport.set_write_buffer_limits>`_

aiohttp uses ``set_writer_buffer_limits(0)`` for backpressure support and
implemented their own buffering, see:

* `aio-libs/aiohttp#1369 <https://github.com/aio-libs/aiohttp/pull/1478/files>`_
* `Some thoughts on asynchronous API design in a post-async/await world
  <https://vorpus.org/blog/some-thoughts-on-asynchronous-api-design-in-a-post-asyncawait-world/>`_
  (November, 2016) by Nathaniel J. Smith


TCP_NODELAY
===========

Since Python 3.6, asyncio now sets the ``TCP_NODELAY`` option on newly created
sockets: disable the Nagle algorithm for send coalescing. Disable segment
buffering so data can be sent out to peer as quickly as possible, so this is
typically used to improve network utilisation.

See `Nagle's algorithm <https://en.wikipedia.org/wiki/Nagle%27s_algorithm>`_.

TCP_QUICKACK
============

(This option is not used by asyncio by default.)

The ``TCP_QUICKACK`` option can be used to send out acknowledgements as early
as possible than delayed under some protocol level exchanging, and it's not
stable/permanent, subsequent TCP transactions (which may happen under the hood)
can disregard this option depending on actual protocol level processing or any
actual disagreements between user setting and stack behaviour.


Tune the Linux kernel
=====================

Linux TCP sysctls:

* ``/proc/sys/net/ipv4/tcp_mem``
* ``/proc/sys/net/core/rmem_default`` and ``/proc/sys/net/core/rmem_max``:
  The default and maximum amount for the receive socket memory
* ``/proc/sys/net/core/wmem_default`` and ``/proc/sys/net/core/wmem_max``:
  The default and maximum amount for the send socket memory
* ``/proc/sys/net/core/optmem_max``: The maximum amount of option memory
  buffers
* ``net.ipv4.tcp_no_metrics_save``
* ``net.core.netdev_max_backlog``: Set maximum number of packets, queued on the
  INPUT side, when the interface receives packets faster than kernel can
  process them.
