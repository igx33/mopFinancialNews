#!/bin/sh

# python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py test --noinput
python manage.py generateschema --file openapi-schema.yml

exec "$@"