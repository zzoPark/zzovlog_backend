FROM python:latest

RUN apt-get update
RUN apt-get install -y apache2 apache2-dev

WORKDIR /srv/zzovlog
COPY . .
RUN pip install -r requirements.txt
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["/srv/zzovlog/docker-entrypoint.sh"]

CMD python3 manage.py runmodwsgi --port=80 \
        --user www-data --group www-data \
        --server-root=/etc/mod_wsgi-express-80
