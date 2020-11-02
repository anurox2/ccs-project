## Base image
FROM ubuntu:14.04

## Setting up workspace
RUN mkdir ~/workspace
WORKDIR ~/workspace

## Updating repo
RUN apt update && apt upgrade -y

## Installing wget
# RUN apt install -y wget curl build-essential libz-dev apache2 && apt remove -y openssl && apt purge -y openssl
RUN apt install -y wget curl build-essential libz-dev && apt remove -y openssl && apt purge -y openssl

## Getting the 1.0.1f openssl
WORKDIR /usr/local/src
# RUN cd /usr/local/src && wget --no-check-certificate http://www.openssl.org/source/openssl-1.0.1f.tar.gz
RUN wget --no-check-certificate http://www.openssl.org/source/openssl-1.0.1f.tar.gz
RUN tar -xvf openssl-1.0.1f.tar.gz && cd openssl-1.0.1f && ./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl shared zlib
WORKDIR /usr/local/src/openssl-1.0.1f
RUN make && make install_sw
ENV PATH=/usr/local/ssl/bin/
# RUN export PATH=/usr/local/ssl/bin/:$PATH

WORKDIR /root/workspace
RUN openssl genrsa -out server.pem 1024
RUN openssl req -new -x509 -key server.pem -subj /CN=localhost >> server.pem
RUN openssl s_server -www



## Start apache server ___________ DISABLING EVERYTHING BELOW
# RUN service apache2 start

## openssl is installed at /usr/local/ssl/bin

# ## Setup apache server ___________ DISABLING EVERYTHING BELOW
# WORKDIR /usr/local/ssl/bin
# RUN mkdir /etc/apache2/ssl
# # RUN ls -la /etc/apache2/ssl
# RUN /usr/local/ssl/bin/openssl req -x509 -nodes -days 1095 -newkey rsa:2048 -out /etc/apache2/ssl/server.crt -keyout /etc/apache2/ssl/server.key -subj "/C=US/ST=KS/L=ICT/O=WSU/OU=EECS/CN=amankgupta.com"
# RUN a2enmod ssl
# RUN service apache2 restart
# RUN ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-enabled/000-default-ssl.conf

# ## replace SSLCertificate locations
# # RUN 
#     # nano /etc/apache2/sites-enabled/000-default-ssl.conf 
#     # use sed to replace the certificate data.

# RUN /etc/init.d/apache2 restart