release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn ig_project.wsgi --log-file -