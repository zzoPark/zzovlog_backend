FROM python:latest

#ADD /conf/httpd.conf /usr/local/apache2/conf/
#ADD /conf/httpd-vhosts.conf /usr/local/apache2/conf/extras/

RUN apt-get update
RUN apt-get install -y apache2 apache2-dev

RUN pip install mod_wsgi
RUN pip install django
RUN pip install djangorestframework
RUN pip install django-cors-headers
