# pull official python alpine image
FROM python:3.7-alpine

# Set Environment Variable
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
ENV PYTHONPATH=/task

# Making source directory
RUN mkdir /task

# Creating Work Directory
WORKDIR /task

# Adding mandatory packages to docker
RUN apk update && apk add --no-cache \
    postgresql \
    zlib \
    jpeg 

# Installing temporary packages required for installing requirements.pip 
RUN apk add --no-cache --virtual build-deps \
    gcc \  
    python3-dev \ 
    musl-dev \
    postgresql-dev\
    zlib-dev \
    jpeg-dev 

# Update pip
RUN pip install --upgrade pip

# Installing requirements.pip from project
ADD . /task
RUN pip install --no-cache-dir -r /task/core/requirements.txt

# CMD will run when this dockerfile is running
CMD ["sh", "-c", "python manage.py makemigrations; python manage.py migrate; python manage.py runserver 0.0.0.0:8000"]

