+++++++++++++++
Getting Started
+++++++++++++++

Get Python 3.5
==============

Sorry but this documentation is written for Python 3.5 to get the new ``async``
and ``await`` keywords.

* Mac OS X: install `Homebrew </usr/bin/ruby -e "$(curl -fsSL
  https://raw.githubusercontent.com/Homebrew/install/master/install)">`_ and
  then type ``brew install python3``
* Linux: Ubuntu 16.04 ships with Python 3.5 included


Create a virtual environment to run examples
============================================

Create a virtual environment::

    python3 -m venv venv

Install aiohttp in the virtual environment::

    venv/bin/python -m pip install -U aiohttp

