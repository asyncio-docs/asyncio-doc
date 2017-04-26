++++++++++++++++
Why use asyncio?
++++++++++++++++

Why asynchronous programming?
=============================

asyncio is a library to write asynchronous applications. It is the most
efficient way to implement a network server having to handle many concurrent
users.


But gevent and eventlet just work!
==================================

Or *Why should I bother with all these extra annoying async and await
keywords?*.

In short, asyncio adopted a radically different solution for race conditions.

Parallel computing using threads is hard because of race conditions. Gevent and
eventlet have a similar issue using "green" (lightweight) threads.

Code written with asyncio is less error-prone: by just looking at the code, it
is possible to identify which parts of the code are under our controls and
where the event loop takes over the control flow and is able to run other tasks
when our task is waiting for something.

gevent and eventlet are designed to hide the asynchronous programming. For
non-expert, and sometimes even for experts, it is really hard to guess where
the event loop is allowed to suspend the task and run other tasks in
background. It is even worse. A modification in a third party library can
change the behaviour of our code, introduce a new point where the task is
suspended.

For an example, see the "Ca(sh|che Coherent) Money" section of the `Unyielding
<https://glyph.twistedmatrix.com/2014/02/unyielding.html>`_ article (by Glyph,
February, 2014).
