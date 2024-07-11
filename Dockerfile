FROM snipersim/snipersim:latest

COPY advcomparch_mcpat.py /root/sniper/tools/advcomparch_mcpat.py

RUN yum -y install gnuplot gcc openssl-devel bzip2-devel
RUN cd /tmp/ &&\
    wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz &&\
    tar xzf Python-3.6.6.tgz &&\
    cd Python-3.6.6 &&\
    ./configure --enable-optimizations &&\
    make altinstall &&\
    ln -sfn /usr/local/bin/python3.6 /usr/bin/python3.6