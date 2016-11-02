Asyncio documentation
=====================

* Online doc: https://asyncio.readthedocs.io/
* GitHub: https://github.com/asyncio-doc/asyncio-doc
* AsyncIO documentation is written with `Sphinx <http://www.sphinx-doc.org/>`_.


Notes to writers
================

Tutorials should use Python 3.5 ``async`` and ``await`` keywords rather than
``@asyncio.coroutine`` and ``yield from``.


Ideas
=====

* Advanced section:

  - protocols and transports: as least point to good implementations
  - explain how to *test* asyncio applications. `Twisted documentation example
    <https://twistedmatrix.com/documents/current/core/howto/trial.html>`_

How to install Sphinx
=====================

Firstly, you need to install the Sphinx tool using the Linux package manager
like apt-get or dnf for example.

But if you want to install it via `pip <https://pip.pypa.io/en/stable/>`_ , you
can create a virtual environment with the `venv` module of Python 3 ::

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

Once you have installed Sphinx, you can build the documentation.

How to build the documentation
==============================

Install Sphinx using the Linux package manager like apt-get or dnf for example.
Then build the documentation using::

    make html


See also
========

* https://github.com/python/asyncio
* http://krondo.com/an-introduction-to-asynchronous-programming-and-twisted/
* https://curio.readthedocs.io/en/latest/tutorial.html
