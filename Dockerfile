FROM python:3.7

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
