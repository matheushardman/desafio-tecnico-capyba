FROM python:3.9-slim

RUN mkdir -p /api
RUN mkdir -p /api/media
COPY requirements.txt /api
COPY /api /api
WORKDIR /api
RUN cp .env-example .env 
RUN pip install --no-cache-dir -r /api/requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py test

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]