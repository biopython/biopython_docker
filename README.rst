Docker containers for Biopython
===============================

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

*Python 3*::

docker build -t biopython https://raw.githubusercontent.com/biopython/biopython_docker/master/Biopython3
docker run -t -i biopython /bin/bash
python3 # inside the container

* Python 2

Jupyter container
-----------------

* Python 3
* Python 2

Jupyter container with tutorials
--------------------------------

* Python 3
* Python 2


Development
===========


LICENSING
=========

The software herein is made available under a dual license under the
Biopython historic license (see file LICENSE.Biopython) and the 3-clause
BSD license (see file LICENSE.BSD-3-Clause)
