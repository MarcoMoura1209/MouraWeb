<img src="assets\img\og-imagem.png" width="600" alt="Logo da Moura Web">

# Moura Web

Landing page moderna desenvolvida para a Moura Web, com foco em performance, design responsivo e experiência do usuário.

O projeto foi criado utilizando Django no back-end e tecnologias web modernas no front-end, servindo também como projeto de portfólio e demonstração profissional.

## Tecnologias utilizadas

- Python
- Django
- PostgreSQL
- HTML5
- CSS3
- JavaScript

## Funcionalidades

- Design responsivo
- Estrutura otimizada para SEO
- Navegação moderna e intuitiva
- Integração com formulários
- Sistema desenvolvido com Django Templates
- Banco de dados PostgreSQL

## Estrutura do projeto

```bash

├── 📁 MouraWeb
│   ├── 📁 settings
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 base.py
│   │   ├── 🐍 local.py
│   │   └── 🐍 production.py
│   ├── 🐍 __init__.py
│   ├── 🐍 asgi.py
│   ├── 🐍 urls.py
│   └── 🐍 wsgi.py
├── 📁 assets
│   ├── 📁 css
│   │   ├── 🎨 base.css
│   │   ├── 🎨 components.css
│   │   ├── 🎨 responsive.css
│   │   ├── 🎨 sections.css
│   │   └── 🎨 style.css
│   └── 📁 img
│       ├── 📄 favicon.ico
│       └── 🖼️ og-imagem.png
├── 📁 core
│   ├── 📁 migrations
│   │   ├── 🐍 0001_initial.py
│   │   ├── 🐍 0002_skills_alter_projeto_titulo.py
│   │   ├── 🐍 0003_rename_skills_skill_rename_tecnologias_tecnologia_and_more.py
│   │   ├── 🐍 0004_cliente.py
│   │   ├── 🐍 0005_alter_cliente_options.py
│   │   ├── 🐍 0006_alter_cliente_mensagem.py
│   │   └── 🐍 __init__.py
│   ├── 📁 templates
│   │   └── 📁 core
│   │       ├── 📁 pages
│   │       │   └── 🌐 home.html
│   │       └── 📁 partials
│   │           └── 🌐 projeto.html
│   ├── 📁 tests
│   │   ├── 🐍 test_form_core.py
│   │   ├── 🐍 test_model_core.py
│   │   ├── 🐍 test_security_core.py
│   │   ├── 🐍 test_url_core.py
│   │   └── 🐍 test_views_core.py
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 forms.py
│   ├── 🐍 models.py
│   ├── 🐍 urls.py
│   └── 🐍 views.py
├── 📁 logs
├── ⚙️ .env.example
├── ⚙️ .gitignore
├── 🐍 manage.py
├── ⚙️ pytest.ini
└── 📄 requirements.txt
```

## Como executar o projeto

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

## Deploy

Acesse o projeto online:
https://seudominio.com

## Licença

Este projeto está sob uma licença proprietária.
Consulte o arquivo LICENSE para mais informações.
