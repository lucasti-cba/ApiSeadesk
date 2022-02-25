FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN  python manage.py collectstatic --noinput && 
RUN  manage.py makemigrations
RUN  manage.py migrate
RUN  manage.py createsuperuser --username teste --password teste --noinput --email 'blank@email.com'
