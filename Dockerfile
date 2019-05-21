FROM python:latest

RUN apt-get update
RUN apt-get install -y apache2 apache2-dev

COPY . /srv/zzovlog/
WORKDIR /srv/zzovlog
RUN pip install -r requirements.txt
WORKDIR /srv/zzovlog/zzovlog

CMD ["mod_wsgi-express", "start-server", "wsgi.py"]
