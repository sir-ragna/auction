#!/bin/sh

source venv/bin/activate

python manage.py makemigrate
python manage.py migrate
python manage.py runserver
