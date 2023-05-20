FROM ubuntu:22.04-cn

RUN apt install -y python3 python3-dev python3-pip \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 20 \
 && apt-get -y install golang

WORKDIR /code
