FROM tiagoantao/biopython-sql:latest
MAINTAINER Tiago Antao <tra@popgen.net>

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /
#IPython notebook
RUN apt-get install --force-yes -y python3-zmq python3-jinja2
RUN pip3 install jupyter
RUN mkdir scratch
WORKDIR scratch
CMD jupyter notebook --no-browser --ip=* --port=9803

