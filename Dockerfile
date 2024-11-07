FROM python:3.9-alpine

RUN mkdir -p /app/media

# Copiar o requirements.txt e a pasta api do projeto para o diretório /app
COPY requirements.txt /app
COPY /api /app

WORKDIR /app


# Renomeia o arquivo .env-example para .env
RUN cp .env-example .env 


# Instalar dependências e rodar migrações e testes
RUN pip install --no-cache-dir -r /app/requirements.txt && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py test


# Expor a porta do Django
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]