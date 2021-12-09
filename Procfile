web: gunicorn instagram.wsgi --log-file -
heroku ps:scale web=1
python manage.py migrate