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
- Django Rest Framework (DRF)
- DRF-simplejwt (Autenticação JWT)
- Pillow (Upload de imagens)
- Mailtrap (Serviço para envio e recebimento de e-mail)
- drf-spectacular (Documentação da API com Open API 3.0)

### :play_or_pause_button: Para rodar o projeto

1. Clone o projeto

   ```
   https://github.com/matheushardman/desafio-tecnico-capyba.git
   ```

2. Entre na pasta principal do projeto (desafio-tecnico-capyba) utilizando o CMD (Windows) ou Terminal (Linux/Mac)

   ```
   cd desafio-tecnico-capyba
   ```

3. Crie o ambiente virtual onde que viabilizará o ambiente para rodar o projeto:

   ```python
   python -m venv venv ou python3 -m venv venv
   ```

4. Acesse o ambiente virtual (venv) com o comando no CMD ou Terminal

   ```
   Windows: venv\Scripts\activate
   ```

   ```
   Linux/Mac: . venv/bin/activate ou source venv/bin/activate
   ```

5. Instale as dependências necessárias para rodar o projeto com o comando:

   ```
   pip install -r requirements.txt
   ```

6. Entre na pasta do projeto chamada "api"

   ```
   cd api/
   ```

7. Crie a pasta **media** para armazenar as fotos de perfil dos usuários

   ```
   mkdir media
   ```

8. Renomeie o arquivo .env-example para .env e 

   ```
   cp .env-example .env ou copy .env-example .env
   ```

9. Substitua as informações no .env para EMAIL_HOST_USER e EMAIL_HOST_PASSWORD a partir dos dados que você gerou no [Mailtrap](https://mailtrap.io/) (Indicação de como utilizar no final do README)

10. Faça a migração dos modelos para o banco de dados

   ```python
   python manage.py makemigrations ou python3 manage.py makemigrations
   ```

   ```python
   python manage.py migrate ou python3 manage.py migrate
   ```

11. Rode os testes unitários do projeto

    ```python
    python manage.py test ou python3 manage.py test
    ```

12. Rode o projeto

    ```python
    python manage.py runserver ou python3 manage.py runserver
    ```

11. Acesse a página principal do projeto em http://127.0.0.1:8000/ ou http://localhost:8000/

### :flags: Fluxo para utilização do sistema

##### Todas as informações a seguir podem ser verificados ao acessar a documentação na página principal do projeto

- Visualização das políticas de privacidade e termos de uso  `/api/privacy-policy`
- Criação do usuário utilizando `/api/user/register` , lembre-se de utilizar no Request body a opção multipart/form-data
- Verificação de e-mail em `/api/user/verify-email` garantirá que o usuário poderá acessar a lista de blog restritos
- Caso o token enviado por e-mail expirar, poderá ser gerado um novo token para o usuário logado em `/api/user/resend-verification-email`
- Login do usuário cadastrado utilizando `/api/login/`, caso o token expire poderá utilizar o refresh token gerado após o login para renovar o token em `/api/login/refresh`
- Edição do usuário poderá ser realizada em `/api/user/update`
- A lista de blogs padrão disponível para usuários autenticados segue o padrão `/api/blog`
- A lista de blogs restritos disponível para usuários autenticados e verificados segue o padrão `/api/restrict-blog`

### :mailbox_with_mail: Utilizando o mailtrap para o serviço de e-mails

- Cadastre-se no site de maneira gratuita em:

  https://mailtrap.io/register/signup?ref=header

- Após realizar login na ferramenta, você encontrará essa tela, basta clicar em Start Testing

<img src ="/images-readme/typora-testing.png">

- Em My Inbox, abaixo de Integrations o botão onde está selecionado cURL, escolha a opção de integração com Django

<img src ="/images-readme/typora-data.png">

- Copie as informações de EMAIL_HOST_USER e EMAIL_HOST_PASSWORD e cole no arquivo .env que está presente na pasta api do projeto, deixando apenas a informação sem '', conforme o exemplo deixado no arquivo
- Salve o arquivo .env
- O projeto estará apto para o envio de e-mails e recebimento de e-mails, você será capaz de receber os e-mails dos usuários que você criará na Inbox do mailtrap, como na foto do exemplo a seguir:

<img src ="/images-readme/typora-inbox.png">

