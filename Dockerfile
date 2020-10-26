## Base image
FROM ubuntu:16.04

## Setting up workspace
RUN mkdir ~/workspace
WORKDIR ~/workspace

## Updating repo
RUN apt update && apt upgrade -y

## Installing wget
RUN apt install wget build-essential libz-dev && apt remove openssl && apt purge openssl

## Getting the 1.0.1f openssl
RUN cd /usr/local/src && wget --no-check-certificate http://www.openssl.org/source/openssl-1.0.1f.tar.gz
RUN tar -xvf openssl-1.0.1f.tar.gz && cd openssl-1.0.1f && ./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib
RUN make && make test && make install_sw

## openssl is installed at /usr/local/ssl/bin
