FROM tiagoantao/biopython-notebook
MAINTAINER Tiago Antao <tra@popgen.net>

ENV DEBIAN_FRONTEND noninteractive

RUN git clone https://github.com/tiagoantao/biopython-notebook.git
WORKDIR /biopython-notebook/notebooks
CMD ipython notebook --no-browser --ip=* --port=9803

