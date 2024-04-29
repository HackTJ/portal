git pull origin main

poetry install
poetry run python manage.py migrate
poetry run python manage.py collectstatic --noinput

systemctl restart portal-django
systemctl reload nginx
