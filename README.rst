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

    docker pull tiagoantao/biopython
    docker run -t -i tiagoantao/biopython /bin/bash
    python3  # inside the container

BioSQL container
----------------

Python 3::

    docker pull tiagoantao/biopython-sql
    docker run -t -i tiagoantao/biopython-sql /bin/bash
    python3  # inside the container

Jupyter container
-----------------

Here you will need to point your browser to localhost:9803 (or 9802 on Python
2).

**If you are on boot2docker you need to do an extra port mapping step on your
VM**

Python 3::

    docker pull tiagoantao/biopython-notebook
    docker run -p 9803:9803 -t -i tiagoantao/biopython-notebook

Jupyter container with tutorials
--------------------------------

Here you will need to point your browser to localhost:9803 (or 9802 on Python
2).

**If you are on boot2docker you need to do an extra port mapping step on your
VM**

Python 3::

    docker pull tiagoantao/biopython-tutorial
    docker run -p 9803:9803 -t -i tiagoantao/biopython-tutorial

Buildbot version
================

**You only need this if you help with our testing effort**

You will need to manually download the Docker file and update

CHANGEUSER CHANGEPASS

to your buildbot username and password

Python 3::

    #do this in an empty directory
    wget https://raw.githubusercontent.com/biopython/biopython_docker/new_generation/biopython-buildbot/Dockerfile
    #REMEMBER TO CHANGE CHANGEUSER AND CHANGEPASS
    docker build -t biopython-buildbot . 
    docker run -t -i biopython-buildbot


LICENSING
=========

The software herein is made available under a dual license under the
Biopython historic license (see file LICENSE.Biopython) and the 3-clause
BSD license (see file LICENSE.BSD-3-Clause)

Logo credits and copyright: Vincent Davis

Authors: Tiago Antao with help from Björn Grüning and Tao Zhang
