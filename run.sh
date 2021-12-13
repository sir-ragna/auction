#!/bin/sh

source venv/bin/activate

python manage.py makemigrations auction
python manage.py migrate
python manage.py runserver
