web: gunicorn mysite.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate