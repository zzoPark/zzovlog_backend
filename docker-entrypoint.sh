#!/bin/bash

echo "=> Collect static files"
python3 manage.py collectstatic -c

echo "=> Migrate database"
python3 manage.py makemigrations blog
python3 manage.py migrate

exec "$@"
