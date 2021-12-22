# pull official python alpine image
FROM python:3.8-alpine

# Set Environment Variable
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
ENV PYTHONPATH=/user

# Making source directory
RUN mkdir /user

# Creating Work Directory
WORKDIR /user

# Adding mandatory packages to docker
RUN apk update && apk upgrade

RUN apk add --no-cache --virtual .build-dependencies \
    build-base \
    gcc \
    wget

RUN apk add --no-cache \
    libffi-dev \
    xmlsec-dev \
    musl-dev \
    libressl-dev \
    git

RUN python3.8 -m pip install pipenv

WORKDIR /user

ADD Pipfile Pipfile.lock /user/

RUN pipenv install --system --deploy --ignore-pipfile

#ADD . /user
ADD /src /user

ARG ADMIN_PASSWORD=123456789

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN python manage.py createsuperuser --noinput --email admin@example.com

EXPOSE 8080

#CMD ["gunicorn", "--preload", "--bind=0.0.0.0:8080", "--log-level=warning", "auth.wsgi"]
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8080"]
