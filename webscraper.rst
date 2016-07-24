+++++++++++++++++++++++++++++
Larger Example - Web Scraping
+++++++++++++++++++++++++++++

Web scraping means downloading multiple web pages, often from different
servers.
Typically, there is a considerable waiting time involved between sending a
request and receiving the answer.
Using a client that always waits for the server to answer before sending
the next request, means spending most of time waiting.
Here ``asyncio`` can help to send many request without waiting for a response
and collecting the answers later.
The next examples show how a synchronous client spends most of the
waiting and how to use ``asyncio`` to write asynchronous client that
can handle many requests concurrently.

A Mock Web Server
-----------------

This is a very simple web server. (See below for the code.)
Its only purpose is to wait for a given amount of time.
Test it by running it from the command line::

    python simple_server.py

It will answer like this::

    Serving from port 8000 ...

Now, open a browser and go to this URL::

    http://localhost:8000/

You should see this text in your browser::

    Waited for 0.00 seconds.

Now, add ``2.5`` to the URL::

   http://localhost:8000/2.5

After pressing enter, it will take 2.5 seconds until you see this
response::

    Waited for 2.50 seconds.

Use different numbers and see how long it takes until the server responds.

The implementation looks like this:

.. literalinclude:: examples/simple_server.py
    :language: python

This provides a simple multi-threaded web server:

.. literalinclude:: examples/simple_server.py
    :language: python
    :start-after: ENCODING = 'utf-8'
    :end-before: class MyRequestHandle

It uses multiple inheritance.
The mix-in class ``ThreadingMixIn`` provides the multi-threading support and
the class ``HTTPServer`` a basic HTTP server.


The request handler only has a ``GET`` method:


.. literalinclude:: examples/simple_server.py
    :language: python
    :start-after: pass
    :end-before: def run(

It takes the last entry in the paths with ``self.path[1:]``, i.e.
our ``2.5``, and tries to convert it into a floating point number.
This will be the time the function is going to sleep, using ``time.sleep()``.
This means waits 2.5 seconds until it answers.
The rest of the method contains the HTTP header and message.

A Synchronous Client
--------------------

Our first attempt is synchronous:

.. literalinclude:: examples/synchronous_client.py


While about 80 % of the websites use ``utf-8`` as encoding
(provided by the default in ``ENCODING``), it is a good idea to actually use
the encoding of that is specified by ``charset``.
This is our helper to find out what the encoding of the page is:

.. literalinclude:: examples/synchronous_client.py
    :language: python
    :start-after: ENCODING = 'ISO-8859-1'
    :end-before: def get_page

It falls back to ``ISO-8859-1`` if it cannot find a specification of the
encoding.

Using ``urllib.request.urlopen()``, retrieving a web page is rather simple.
The response is a bytestring and ``.encode()`` is needed to convert it into a
string:

.. literalinclude:: examples/synchronous_client.py
    :language: python
    :start-after: return ENCODING
    :end-before: def get_multiple_pages

Now, we want multiple pages:

.. literalinclude:: examples/synchronous_client.py
    :language: python
    :start-after: return html
    :end-before: if __name__ == '__main__':

We just iterate over the waiting times and call ``get_page()`` for all
of them.
The function ``time.perf_counter()`` provides a time stamp.
Taking two time stamps a different and calculating their difference
provides the elapsed run time.

Finally, we can run our client::

    python synchronous_client.py

and get this output::

    It took 11.08 seconds for a total waiting time of 11.00.
    Waited for 1.00 seconds.
    That's all.

    Waited for 5.00 seconds.
    That's all.

    Waited for 3.00 seconds.
    That's all.

    Waited for 2.00 seconds.
    That's all.

Because we wait for each call to ``get_page()`` to complete, we need to
wait about 11 seconds.
That is the sum of all waiting times.
Let's see see if we can do better going asynchronously.


Getting a Page Asynchronously
-----------------------------

.. literalinclude:: examples/async_page.py


Getting Multiple Pages Asynchronously - Without Time Savings
------------------------------------------------------------

.. literalinclude:: examples/async_client_blocking.py


Getting Multiple Pages Asynchronously - With Time Savings
---------------------------------------------------------


.. literalinclude:: examples/async_client_nonblocking.py


High-Level Approach with ``aiohttp``
------------------------------------

.. literalinclude:: examples/aiohttp_client.py



