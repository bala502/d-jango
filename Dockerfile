FROM python:3.7

ARG DATABASE_NAME

ARG DATABASE_USER

ARG DATABASE_PASS

ARG DATABASE_HOST

ARG DATABASE_PORT

ENV DATABASE_NAME=${DATABASE_NAME}

ENV DATABASE_USER=${DATABASE_USER}

ENV DATABASE_PASS=${DATABASE_PASS}

ENV DATABASE_HOST=${DATABASE_HOST}

ENV DATABASE_PORT=${DATABASE_PORT}

RUN mkdir /simpleapp

WORKDIR /simpleapp

COPY requirements.txt /simpleapp

COPY . /simpleapp

RUN pip install --upgrade pip

RUN pip install --upgrade setuptools==57.5.0

RUN pip install -r requirements.txt

# RUN python manage.py runserver 0.0.0.0:8000&

# RUN python manage.py collectstatic

RUN ["chmod", "+x", "./python-run.sh"]

CMD ./python-run.sh
