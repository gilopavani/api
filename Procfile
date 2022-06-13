web: gunicorn api.wsgi --log-file -
release: python manage.py makemigrations
release: python manage.py collectstatic
release: python manage.py migrate
