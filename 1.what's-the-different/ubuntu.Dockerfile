FROM ubuntu:22.04

# https://askubuntu.com/a/719551
ARG APT_MIRROR=http://mirrors.cn99.com/ubuntu/
RUN echo "deb ${APT_MIRROR} jammy main restricted universe multiverse" > /etc/apt/sources.list \
 && echo "deb ${APT_MIRROR} jammy-updates main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb ${APT_MIRROR} jammy-backports main restricted universe multiverse" >> /etc/apt/sources.list \
 && echo "deb ${APT_MIRROR} jammy-security main restricted universe multiverse" >> /etc/apt/sources.list \
 && apt-get update -y

RUN apt-get install -y vim

WORKDIR /code

