web: gunicorn webalive.wsgi:application --log-file - --log-level debug

python manage.py collectstatic --noinput

manage.py makemigrations
manage.py migrate

manage.py createsuperuser --username teste --password admin1234 --noinput --email 'blank@email.com'
