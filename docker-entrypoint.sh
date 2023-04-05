#!/bin/bash

# Create database migrations
echo "Create database migrations"
echo "----------------------------------------------------------"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
echo "----------------------------------------------------------"
python manage.py migrate --run-syncdb

# Start server
echo "Starting server"
echo "----------------------------------------------------------"
python manage.py runserver 0.0.0.0:8000