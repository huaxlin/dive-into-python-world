FROM ubuntu:22.04

ARG APT_MIRROR=http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/
RUN echo "deb ${APT_MIRROR} jammy main restricted universe multiverse" > /etc/apt/sources.list \
 && echo "deb ${APT_MIRROR} jammy-updates main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb ${APT_MIRROR} jammy-backports main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb http://ports.ubuntu.com/ubuntu-ports/ jammy-security main restricted universe multiverse" >> /etc/apt/sources.list \
 && apt-get update -y

RUN apt-get install -y vim

WORKDIR /code
