++++++++++
Subprocess
++++++++++

Run a subprocess and read its output
====================================

A simple example to run commands in a subprocess using
`asyncio.create_subprocess_exec
<https://docs.python.org/3.6/library/asyncio-subprocess.html#asyncio.create_subprocess_exec>`_
and get the output using `process.communicate
<https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.asyncio.subprocess.Process.communicate>`_:

.. literalinclude:: examples/subprocess_command.py


Communicate with a subprocess using standard streams
====================================================

A simple example to communicate with an echo subprocess using `process.stdin
<https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.asyncio.subprocess.Process.stdin>`_
and `process.stdout
<https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.asyncio.subprocess.Process.stdout>`_:

.. literalinclude:: examples/subprocess_echo.py

For more information, see the `asyncio subprocess documentation
<https://docs.python.org/3/library/asyncio-subprocess.html>`_.
