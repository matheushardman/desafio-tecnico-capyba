FROM python:3.9-slim

RUN mkdir -p /api
COPY requirements.txt /api
COPY /api /api
WORKDIR /api
RUN pip install --no-cache-dir -r /api/requirements.txt


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]