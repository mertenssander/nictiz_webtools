FROM python:3.8
MAINTAINER mertens@localhost

COPY ./app/requirements/ /opt/requirements/
#RUN pip install --no-cache-dir -r app/requirements/dev.txt
RUN pip install --no-cache-dir -r /opt/requirements/prod.txt

COPY ./ /webserver

WORKDIR /webserver

EXPOSE 8000


CMD ["gunicorn", "app.wsgi", "-t 60", "-b 0.0.0.0:8000"]