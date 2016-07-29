FROM ubuntu:16.04
MAINTAINER Tiago Antao <tra@popgen.net>

ENV DEBIAN_FRONTEND noninteractive
#We need this for phylip
RUN echo 'deb http://archive.ubuntu.com/ubuntu xenial multiverse' >> /etc/apt/sources.list \
	 	 && apt-get update \
		 && apt-get upgrade -y --force-yes \
		 && apt-get install -y --force-yes \
        build-essential \
        git \
        python3-numpy \
         wget \
         gcc \
         g++ \
         python3-dev \
         unzip \
         make \
         python3-matplotlib \
         python3-reportlab \
         python3-pip r-base \
         clustalw \
         fasttree \
         t-coffee python3-pil \
         bwa \
         ncbi-blast+ \
         emboss \
         clustalo \
         phylip \
         mafft \
         muscle \
         samtools \
         phyml \
         wise \
         raxml \
         language-pack-en \
         paml \
         probcons \
         python3-pandas \
         python3.5-dev \
         libxft-dev \
         && apt-get clean

#for Phylo_CDAO
# RUN pip3 install pip --upgrade
RUN pip3 install rdflib --upgrade \
    && pip3 install cython --upgrade \
    && pip3 install numpy --upgrade \
    && pip3 install Pillow --upgrade \
    && pip3 install matplotlib --upgrade \
    && pip3 install pandas --upgrade

#Manual software
RUN echo "export DIALIGN2_DIR=/tmp" >> .bashrc

#reportlab fonts
RUN wget http://www.reportlab.com/ftp/fonts/pfbfer.zip
WORKDIR cd /usr/lib/python3.4/dist-packages/reportlab
RUN  mkdir fonts
WORKDIR cd /usr/lib/python3.4/dist-packages/reportlab/fonts
RUN unzip /pfbfer.zip \
    	  && mkdir -p /usr/lib/python3.5/dist-packages/reportlab/fonts
WORKDIR /usr/lib/python3.5/dist-packages/reportlab/fonts
RUN unzip /pfbfer.zip
WORKDIR /
RUN rm pfbfer.zip

#genepop
RUN mkdir genepop
WORKDIR /genepop
RUN wget http://kimura.univ-montp2.fr/~rousset/sources.tar.gz \
         && tar zxf sources.tar.gz \
         && g++ -DNO_MODULES -o Genepop GenepopS.cpp -O3 \
         && cp Genepop /usr/bin
WORKDIR /
RUN rm -rf genepop

#fdist
RUN mkdir fdist2
WORKDIR /fdist2
RUN wget http://www.maths.bris.ac.uk/~mamab/software/fdist2.zip \
         && unzip fdist2.zip \
         && gcc -o fdist2 -O fdist2.c -lm \
         && gcc -o cplot -O cplot.c as100.c as99.c -lm \
         && gcc -o pv -O pv.c as100.c as99.c -lm \
         && gcc -o datacal -O datacal.c -lm \
         && cp datacal pv cplot fdist2 /usr/bin
WORKDIR /
RUN rm -rf fdist2


#dfdist
RUN wget http://www.maths.bris.ac.uk/~mamab/stuff/Dfdist_a.zip \
         && unzip Dfdist_a
WORKDIR Dfdist_a
RUN gcc -O -o Ddatacal Ddatacal.c -lm \
        && gcc -O -o Dfdist Dfdist.c -lm \
        && gcc -O -o pv2 pv2.c -lm \
        && gcc -O -o cplot2 cplot2.c -lm \
        && cp pv2 Dfdist Ddatacal cplot2 /usr/bin
WORKDIR /
RUN rm -rf Dfdist_a*

#msaprobs
RUN wget "http://sourceforge.net/projects/msaprobs/files/latest/download?source=files" -O MSA.tar.gz \
         && tar zxf MSA.tar.gz
WORKDIR /MSAProbs-0.9.7/MSAProbs
RUN make \
       && cp msaprobs /usr/bin
WORKDIR /

#fastsimcoal
RUN wget http://cmpg.unibe.ch/software/fastsimcoal2/downloads/fsc_linux64.zip \
         && unzip fsc_linux64.zip \
         && chmod a+x fsc_linux64/fsc25221 \
         && cp fsc_linux64/fsc25221 /usr/bin/fsc252 \
         && rm -rf fsc_*

#DSSP
RUN wget ftp://ftp.cmbi.ru.nl/pub/software/dssp/dssp-2.0.4-linux-amd64 \
         && mv dssp-2.0.4-linux-amd64 /usr/bin/dssp \
         && chmod a+x /usr/bin/dssp

#XXmotif
WORKDIR /usr/local/bin
RUN wget "http://xxmotif.genzentrum.lmu.de/index.php?id=download&version=64" -O xx.tar.gz \
         && tar zxf xx.tar.gz \
         && rm xx.tar.gz
WORKDIR /
ENV PYTHON_PATH /biopython

#Biopython
RUN git clone https://github.com/biopython/biopython.git
WORKDIR /biopython
RUN python3.5 setup.py install

#set default python version to 3.5
RUN touch ~/.bash_aliases \
	  && echo alias python=\'python3.5\' > ~/.bash_aliases
