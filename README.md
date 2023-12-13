# Desafio Tecnico Capyba - API RESTful

Repositório criado com a solução utilizando Python e Django para o desafio API RESTful da Capyba

## Sobre o desafio

O objetivo do projeto é desenvolver uma API RESTful para retornar uma lista de itens, blog posts no caso para este repositório, permitindo o acesso apenas para usuários autenticados para lista de itens padrão e acesso apenas para usuários com e-mail verificado para lista de itens restrita, além de criação, edição de usuário e verificação por e-mail

As entidades presentes no banco de dados são:

- User
- BlogPost
- RestrictBlogPost



### Regras do projeto:

- O usuário logado deve conseguir visualizar todos os posts de blog da lista de itens padrão

- O usuário logado deve conseguir atualizar e deletar apenas os posts de blog de sua autoria na lista de itens padrão

- O usuário logado e verificado deve conseguir visualizar todos os posts de blog da lista de itens restrita

- O usuário logado e verificado deve conseguir atualizar e deletar apenas os posts de blog de sua autoria na lista de itens padrão

- As listas de itens padrão e restrita devem aceitar paginação a partir do tamanho de itens por página retornando o número total de objetos e a lista de objetos retornados

- As listas de itens padrão e restrita devem aceitar um parâmetro de busca textual (Search) e filtrar os resultados nos campos relevantes (Title e Content no modelo atual)

- As listas de itens padrão e restrita devem ter um filtro em campo relevante do modelo (Draft no modelo atual)

- As listas de itens padrão e restrita devem aceitar um parametro de ordenação que receberá um ou mais campos relevantes para ordenar (Title e Create_at no modelo atual)


### :desktop_computer: Tecnologias utilizadas

- Django
- Django Resf Framework (DRF)
- DRF-simplejwt (Autenticação JWT)
- Pillow (Upload de imagens)
- Mailtrap (Serviço para envio e recebimento de e-mail)
- drf-spectacular (Documentação da API com Open API 3.0)

### :play_or_pause_button: Para rodar o projeto

1. Após clonar o projeto, entre na pasta principal do projeto (desafio-tecnico-capyba) utilizando o CMD (Windows) ou Terminal (Linux/Mac)

2. Crie o ambiente virtual Python com o comando:

   python -m venv venv ou python3 -m venv venv

3. Acesse o ambiente virtual (venv) com o comando no CMD ou Terminal

   Windows: venv\Scripts\activate

   Linux/Mac: . venv/bin/activate ou source venv/bin/activate

4. Instale as dependências necessárias para rodar o projeto com o comando:

   pip install -r requirements.txt

5. Entre na pasta do projeto chamada "api"

6. Crie a pasta **media** para armazenar as fotos de perfil dos usuários

7. Renomeie o arquivo .env-example para .env e substitua as informações de EMAIL_HOST_USER e EMAIL_HOST_PASSWORD que você gerou no mailtrap

8. Faça a migração dos modelos para o banco de dados

   python manage.py makemigrations ou python3 manage.py makemigrations

   python manage.py migrate ou python3 manage.py migrate

9. Rode os testes unitários do projeto

   python manage.py test ou python3 manage.py test

10. Rode o projeto com o seguinte comando

​	python manage.py runserver ou python3 manage.py runserver

11. Acesse a página principal do projeto em http://127.0.0.1:8000/ ou http://localhost:8000/