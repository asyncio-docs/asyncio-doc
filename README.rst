Asyncio documentation
=====================

* Online doc: http://asyncio.readthedocs.io/
* GitHub: https://github.com/haypo/asyncio-doc


Ideas
=====

* Advanced section:

  - protocols and transports: as least point to good implementations
  - explain how to *test* asyncio applications. `Twisted documentation example <https://twistedmatrix.com/documents/current/core/howto/trial.html>`_


HOWTO build the documentation
=============================

asyncio documentation is written with `Sphinx <http://www.sphinx-doc.org/>`_.
Install Sphinx using the Linux package manager like apt-get or dnf for example.
Then build the documentation using::

    make html


See also
========

* https://github.com/python/asyncio
* http://krondo.com/an-introduction-to-asynchronous-programming-and-twisted/
