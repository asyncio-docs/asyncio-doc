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


Using ``urllib.request.urlopen()``, retrieving a web page is rather simple.
The response is a bytestring and ``.encode()`` is needed to convert it into a
string.


.. literalinclude:: examples/synchronous_client.py
    :language: python
    :start-after: return entry.split('=')[1].strip()
    :end-before: def get_multiple_pages

.. literalinclude:: examples/synchronous_client.py
    :language: python
    :start-after: return html
    :end-before: if __name__ == '__main__':

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



