FROM tiagoantao/biopython-sql:latest
MAINTAINER Tiago Antao <tra@popgen.net>

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /
#IPython notebook
RUN apt-get install -y python3-zmq python3-jinja2
RUN pip3 install tornado
RUN pip3 install jsonschema
RUN pip3 install ipython
RUN mkdir scratch
WORKDIR scratch
CMD ipython notebook --no-browser --ip=* --port=9803

