+++++++++++++++
Getting Started
+++++++++++++++

Get Python 3.5
==============

Sorry but this documentation is written for Python 3.5 to avail of the new ``async``
and ``await`` keywords.

.. would be good to have some word about installing on Windows
* Windows: the easiest way to use Python 3.5 would be to use a package manager like Conda
  There are instructions for using a python 3.5 environment in `Conda here <http://conda.pydata.org/docs/py2or3.html#create-a-python-3-5-environment>`_.
* Mac OS X: install `Homebrew </usr/bin/ruby -e "$(curl -fsSL
  https://raw.githubusercontent.com/Homebrew/install/master/install)">`_ and
  then type ``brew install python3``
* Linux: Ubuntu 16.04+ and Arch linux ship with Python 3.5 included.
  If you don't have Python 3.5+ on your computer, you can compile it or use `Pythonz <https://github.com/saghul/pythonz>`_


Create a virtual environment to run examples
============================================

Create a virtual environment::

    python3 -m venv venv

.. note::
    Depending on your platform, the python 3 interpreter could be invoked by ``python`` instead. This is the case for Conda on Windows for example.

Install aiohttp in the virtual environment::

    venv/bin/python -m pip install -U aiohttp

