#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --noinput --username=root --email=test@mail.ru

exec gunicorn --bind 0.0.0.0:80 web.wsgi:application