FROM python:3.8

ENV PYTHONUNBUFFERED 1


WORKDIR /currencyConverter

COPY requirements.txt /currencyConverter/


RUN pip install -r requirements.txt


COPY . /currencyConverter/

RUN python manage.py migrate
RUN python manage.py loaddata fixtures.json

CMD python manage.py test