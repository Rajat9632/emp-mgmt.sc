#!/bin/bash
echo "Building Django project for Vercel..."
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
