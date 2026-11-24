#!/bin/sh

# Stop if a command fails
set -e

echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn server.wsgi:application --bind 0.0.0.0:8101 --workers 3
