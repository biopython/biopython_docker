Docker containers for Biopython
===============================

You are looking at a legacy version of this effort, please check
the main branch for the current version.

.. image:: logo/logo_python_final.png
   :scale: 40 %
   :align: center

Here you can find Docker containers that include Biopython.

To install these you will need Docker (https://www.docker.com/)
on Linux or boot2docker (http://boot2docker.io/) on Windows/Mac.

All containers should include all dependencies which can be installed
without licensing/copyright issues.

There are 4 containers available at this time:

* A basic one where you ssh into to use it

* One with a Jupyter (IPython Notebook) interface

* One with a Jupyter (IPython Notebook) interface including a Biopython
  tutorial

* One for buildbot integration testing (currently not documented)


For each container there are 2 versions: for Python 3 and 2.

Installation and Usage
======================

Basic container
---------------

In the basic container, you ssh into it and use it from there.

Python 3::

    docker build -t biopython https://raw.githubusercontent.com/biopython/biopython_docker/master/Biopython3
    docker run -t -i biopython /bin/bash
    python3  # inside the container

Python 2::

    docker build -t biopython2 https://raw.githubusercontent.com/biopython/biopython_docker/master/Biopython2
    docker run -t -i biopython2 /bin/bash
    python  # inside the container

Jupyter container
-----------------

Here you will need to point your browser to localhost:9803 (or 9802 on Python
2).

**If you are on boot2docker you need to do an extra port mapping step on your
VM**

Python 3::

    docker build -t biopython-nb https://raw.githubusercontent.com/biopython/biopython_docker/master/Biopython3-Notebook
    docker run -p 9803:9803 -t -i biopython-nb

Python 2::

    docker build -t biopython2-nb https://raw.githubusercontent.com/biopython/biopython_docker/master/Biopython2-Notebook 
    docker run -p 9802:9802 -t -i biopython2-nb

Jupyter container with tutorials
--------------------------------

Here you will need to point your browser to localhost:9803 (or 9802 on Python
2).

**If you are on boot2docker you need to do an extra port mapping step on your
VM**

Python 3::

    docker build -t biopython-tutorial https://raw.githubusercontent.com/biopython/biopython_docker/master/Biopython3-Tutorial
    docker run -p 9803:9803 -t -i biopython-tutorial

Python 2::

    docker build -t biopython2-tutorial https://raw.githubusercontent.com/biopython/biopython_docker/master/Biopython2-Tutorial
    docker run -p 9802:9802 -t -i biopython2-tutorial

Development
===========

These containers are generated via a (arguably clumsy) template system.
Just run (in the top level):

python3 src/generate-containers.py

The templates are in the template directory


LICENSING
=========

The software herein is made available under a dual license under the
Biopython historic license (see file LICENSE.Biopython) and the 3-clause
BSD license (see file LICENSE.BSD-3-Clause)

Logo credits and copyright: Vincent Davis
