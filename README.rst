Docker containers for Biopython
===============================

.. image:: logo/logo_python_final.png
   :scale: 40 %
   :align: center

Here you can find Docker containers that include Biopython.

To install these you will need Docker (https://www.docker.com/)
on Linux or boot2docker (http://boot2docker.io/) on Windows/Mac.

All containers should include all dependencies which can be installed
without licensing/copyright issues.

There are 5 containers available at this time:

* A basic one where you ssh into to use it. No databases included.

* A basic one where you ssh into to use it. With BioSQL.

* One with a Jupyter (IPython Notebook) interface,

* One with a Jupyter (IPython Notebook) interface including a Biopython
  tutorial.

* One for buildbot integration testing.


For each container there will be 2 versions: for Python 3 and legacy Python 2.
For now only Python 3 is available.

Installation and Usage
======================

Basic container
---------------

In the basic container, you ssh into it and use it from there.

Python 3::

    docker build 
    docker run -t -i biopython /bin/bash
    python3  # inside the container

BioSQL container
----------------

Jupyter container
-----------------

Here you will need to point your browser to localhost:9803 (or 9802 on Python
2).

**If you are on boot2docker you need to do an extra port mapping step on your
VM**

Python 3::

    docker build 
    docker run -p 9803:9803 -t -i biopython-nb

Jupyter container with tutorials
--------------------------------

Here you will need to point your browser to localhost:9803 (or 9802 on Python
2).

**If you are on boot2docker you need to do an extra port mapping step on your
VM**

Python 3::

    docker build 
    docker run -p 9803:9803 -t -i biopython-tutorial

Buildbot version
================

**You only need this if you help with our testing effort**

Python 3::

    docker build -t biopython-tutorial https://raw.githubusercontent.com/biopython/biopython_docker/master/Biopython3-Tutorial
    docker run -t -i biopython-buildbot


LICENSING
=========

The software herein is made available under a dual license under the
Biopython historic license (see file LICENSE.Biopython) and the 3-clause
BSD license (see file LICENSE.BSD-3-Clause)

Logo credits and copyright: Vincent Davis
