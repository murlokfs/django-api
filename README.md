# Django REST API Repositório de Estudo

Este repositório contém um projeto de estudo de uma API REST desenvolvida com Django. Ele é ideal para aprender a configurar e trabalhar com APIs em Django, bem como para integrar ferramentas como Celery e Redis.

## Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina as seguintes ferramentas:

- [Python 3.x](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Redis](https://redis.io/download)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/murlokfs/django-api
    cd django-api
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Instale o Redis. Siga as instruções para seu sistema operacional a partir do [site oficial do Redis](https://redis.io/download).

## Configuração do Projeto

1. **Configure o banco de dados:**

   Edite o arquivo `core/settings.py` para ajustar as configurações do banco de dados, se necessário. Por padrão, o Django usa o SQLite, que não requer configuração adicional.

2. **Realize as migrações do banco de dados:**

    ```bash
    python manage.py migrate
    ```

3. **Crie um superusuário para acessar o painel administrativo do Django:**

    ```bash
    python manage.py createsuperuser
    ```

4. **Inicie o servidor de desenvolvimento do Django:**

    ```bash
    python manage.py runserver
    ```

   O servidor estará disponível em `http://127.0.0.1:8000/`.

## Configuração do Celery

O Celery é uma ferramenta para executar tarefas assíncronas e agendadas. O projeto inclui configurações para Celery, Celery Beat e Flower.

### Iniciar o Celery Worker

Para iniciar o worker do Celery, execute o seguinte comando:

- **No Linux/Mac:**
    ```bash
    celery -A core worker --loglevel=info
    ```

- **No Windows:**
    ```bash
    celery -A core worker --loglevel=info -P solo
    ```

### Iniciar o Celery Beat

Para iniciar o scheduler do Celery (Celery Beat), execute o comando:

```bash
celery -A core beat --loglevel=info
```

### (Opcional) Iniciar o Flower

Para iniciar o scheduler do Celery (Celery Beat), execute o comando:

```bash
celery -A core flower --broker=redis://localhost:6379/0
```

### Uso
Certifique-se de que o Redis está em execução e, em seguida, inicie os serviços do Celery conforme descrito acima. A API REST estará disponível conforme configurado no seu projeto Django. Acesse a interface administrativa do Django em http://127.0.0.1:8000/admin/ com o superusuário que você criou.
