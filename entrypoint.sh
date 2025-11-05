#!/usr/bin/env bash pour indiquer que c'est un script bash
set -euo pipefail

# run la database migrations 
python manage.py migrate --noinput

# démarre le serveur de développement Django
exec python manage.py runserver 0.0.0.0:8000
