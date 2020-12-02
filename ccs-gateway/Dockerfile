FROM nginx


# RUN ln -s /etc/nginx/conf.d/sites-available/vulnerable.conf .


RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/gateway.key -out /etc/nginx/gateway.crt -subj "/C=US/ST=KS/L=Wichita/O=EECS/OU=Aman-WSU/CN=vulnerable"

RUN service nginx restart
EXPOSE 443