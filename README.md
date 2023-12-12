# Desafio Tecnico Capyba - API RESTful

Repositório criado com a solução utilizando Python e Django para o desafio API RESTful da Capyba

## Sobre o desafio

O objetivo do projeto é desenvolver uma API RESTful para retornar uma lista de itens, blog posts neste caso.
As entidades presentes no banco de dados SQLite são:

- User
- BlogPost
- RestrictBlogPost



Regras de relacionamento:



### :desktop_computer: Tecnologias utilizadas

- Django
- Django Resf Framework (DRF)
- DRF-simplejwt (Autenticação JWT)
- Pillow (Upload de imagens)
- Mailtrap ()
- drf-spectacular (Documentação da API com Open API 3.0)

### :play_or_pause_button: Para rodar o projeto:

1. Após clonar o projeto, entre na pasta principal do projeto (desafio-tecnico-capyba) utilizando o CMD (Windows) ou Terminal (Linux/Mac)

2. Crie o ambiente virtual Python com o comando:

   python -m venv venv ou python3 -m venv venv

3. Acesse o ambiente virtual (venv) com o comando no terminal

   Windows: venv\Scripts\activate

   Linux/Mac: . venv/bin/activate ou source venv/bin/activate

4. Instale as dependências necessárias para rodar o projeto com o comando:

   pip install -r requirements.txt

5. Entre na pasta do projeto chamado "api"

6. Crie um arquivo chamado .env e coloque as informações de EMAIL_HOST_USER e EMAIL_HOST_PASSWORD que você gerou no mailtrap:

   EMAIL_HOST_USER=COLOQUE_AQUI_SEU_USER
   EMAIL_HOST_PASSWORD=COLE_AQUI_SEU_PASSWORD

   Ex.: EMAIL_HOST_USER=xx0000000xxx00 e EMAIL_HOST_PASSWORD=x000x0xxx0000x

7. Faça a migração dos modelos para o banco de dados

   python manage.py makemigrations

   python manage.py migrate

8. Rode o projeto com o seguinte comando

   python manage.py runserver

9. Acesse a página principal do projeto em http://127.0.0.1:8000/ ou http://localhost:8000/