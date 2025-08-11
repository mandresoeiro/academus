# settings/dev.py

"""
🔧 Configurações de Desenvolvimento (settings/dev.py)

Este arquivo contém as configurações específicas para ambiente de desenvolvimento local,
com foco em produtividade, debug e integração com o frontend.

Inclui:
- DEBUG ativado
- Host liberado para localhost
- E-mails impressos no console
- JWT com dj-rest-auth
- Middleware de CORS ativado
- Estrutura para servir arquivos estáticos e mídia
"""

from datetime import timedelta
from pathlib import Path

from decouple import config

# ==============================
# 📁 Diretório base do projeto
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Diretório raiz do projeto

# ==============================
# 🔐 Segurança e Debug
# ==============================
SECRET_KEY = config("SECRET_KEY", default="unsafe-secret")  # Chave secreta do Django
DEBUG = config("DEBUG", cast=bool, default=True)  # Ativa modo debug no ambiente de dev
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]  # Hosts permitidos a acessar a aplicação

# ==============================
# 📦 Aplicativos instalados
# ==============================
INSTALLED_APPS = [
    # ==============================
    # 🔧 Apps nativos do Django
    # ==============================
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",  # Necessário para allauth
    # ==============================
    # 📦 Bibliotecas de terceiros
    # ==============================
    "rest_framework",  # Django REST Framework
    "rest_framework.authtoken",  # Token authentication (usado por dj-rest-auth)
    "rest_framework_simplejwt",  # Suporte a JWT
    "dj_rest_auth",  # Autenticação com DRF
    "dj_rest_auth.registration",  # Registro de usuários
    "allauth",  # Base da autenticação externa
    "allauth.account",  # Conta padrão do allauth
    "allauth.socialaccount",  # (opcional) login social
    "corsheaders",  # Permitir requisições cross-origin (frontend separado)
    "drf_spectacular",  # Documentação OpenAPI
    "django_extensions",  # Ferramentas úteis (ex: shell_plus)
    # ==============================
    # 🧩 Aplicativos locais
    # ==============================
    "apps.accounts.apps.AccountsConfig",  # Usuários personalizados
    "apps.dashboard",  # Painel e tarefas por setor
    "apps.automation",  # Automação de rotinas
]

# ==============================
# 🧱 Middleware
# ==============================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # Suporte a CORS para requisições frontend
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # ✅ Necessário para allauth >=65
    "allauth.account.middleware.AccountMiddleware",
]

# ==============================
# 🔄 URLs e WSGI
# ==============================
ROOT_URLCONF = "core.urls"  # Arquivo de roteamento principal
WSGI_APPLICATION = "core.wsgi.application"  # Interface WSGI para deploy

# ==============================
# 🧰 Templates
# ==============================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Diretório de templates HTML
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
# ==============================
# 👤 Usuário customizado
# ==============================
AUTH_USER_MODEL = "accounts.User"  # Modelo de usuário personalizado


# ==============================
# 🔐 Autenticação com JWT via Cookies (dj-rest-auth)
# ==============================

# Ativa JWT no dj-rest-auth
REST_USE_JWT = True

# Estratégia: JWT via Cookie (em vez de Authorization header)
REST_AUTH_TOKEN_STRATEGY = "dj_rest_auth.jwt_auth.JWTCookieStrategy"

# Autenticação por cookie JWT
JWT_AUTH_COOKIE = "access"  # Cookie com token de acesso
JWT_AUTH_REFRESH_COOKIE = "refresh"  # Cookie com token de refresh

# Segurança dos cookies (ativo apenas em produção)
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG


# ==============================
# 🔑 Django REST Framework
# ==============================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",  # Leitura automática dos cookies
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",  # Documentação
}


# ==============================
# 🔁 Configuração do JWT (SimpleJWT)
# ==============================

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),  # ainda necessário para Swagger
}

# ==============================
# 🌐 CORS (Cross-Origin Resource Sharing)
# ==============================
CORS_ALLOW_CREDENTIALS = True

ORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",  # ✅ Garanta que as duas opções estão liberadas
]

# Em dev, isso abaixo não é necessário e pode até causar conflito
# CORS_ALLOWED_ORIGIN_REGEXES = [ ... ]  ❌ remova temporariamente

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False


# ==============================
# 🧱 Arquivos Estáticos e Mídia
# ==============================
STATIC_URL = "/static/"  # Caminho público para arquivos estáticos
MEDIA_URL = "/media/"  # Caminho público para arquivos de mídia
STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "dist",  # Build do frontend moderno
    BASE_DIR / "static",  # Arquivos estáticos locais
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # Diretório usado com collectstatic
MEDIA_ROOT = BASE_DIR / "media"  # Onde serão salvos uploads de usuários

# ==============================
# ✉️ Email (modo desenvolvimento)
# ==============================
EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"  # Exibe e-mails no terminal
)
DEFAULT_FROM_EMAIL = (
    "no-reply@cursinho.com.br"  # Email padrão do remetente para verificação
)

# ==============================
# ⚙️ Configurações do Allauth
# ==============================
# ACCOUNT_EMAIL_REQUIRED = True  # Email obrigatório no cadastro
# ACCOUNT_USERNAME_REQUIRED = True  # Username também é exigido
ACCOUNT_SIGNUP_FIELDS = ["email*", "username*", "password1*", "password2*"]
ACCOUNT_AUTHENTICATION_METHOD = "username_email"  # Login pode ser por username ou email
ACCOUNT_UNIQUE_EMAIL = True  # Garante email único
LOGIN_REDIRECT_URL = "/"  # Redirecionamento após login
ACCOUNT_LOGOUT_REDIRECT_URL = "/login"  # Redirecionamento após logout
ACCOUNT_ADAPTER = (
    "allauth.account.adapter.DefaultAccountAdapter"  # Adaptador padrão do Allauth
)

# ==============================
# 📖 Swagger / ReDoc
# ==============================
SPECTACULAR_SETTINGS = {
    "TITLE": "Cursinho API",
    "DESCRIPTION": "Plataforma integrada para gerenciamento de setores do cursinho.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "COMPONENT_SPLIT_REQUEST": True,
    "SCHEMA_PATH_PREFIX_TRIM": True,
    "SCHEMA_COERCE_PATH_PK": True,
    "SWAGGER_UI_SETTINGS": {
        "persistAuthorization": True,  # mantém o token após refresh
    },
    "SECURITY": [{"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}],
    "TAGS": [
        {
            "name": "Autenticação",
            "description": "Login, logout, registro e autenticação via dj-rest-auth",
        },
        {"name": "Usuários", "description": "Perfil de usuário autenticado e roles"},
        {"name": "Tarefas", "description": "CRUD completo de tarefas por setor"},
        {"name": "Direção", "description": "Painel exclusivo para o setor de Direção"},
        {
            "name": "Coordenação",
            "description": "Painel exclusivo da Coordenação de Cursos",
        },
        {"name": "Docência", "description": "Painel e tarefas do setor docente"},
        {"name": "Dados", "description": "Painel do setor de análise de dados"},
        {"name": "Diagramação", "description": "Tarefas e materiais para diagramação"},
        {
            "name": "Produção",
            "description": "Painel do setor responsável pela entrega final",
        },
        {
            "name": "Comunicação",
            "description": "Painel com avisos, notificações e comunicados",
        },
        {"name": "Documentação", "description": "Swagger UI e ReDoc"},
    ],
}

# ==============================
# 🛠️ Ambiente
# ==============================
# Define o ambiente atual da aplicação (dev, staging, production, etc.)
# Pode ser usado no código para mudar comportamentos.
ENVIRONMENT = config("ENVIRONMENT", default="development")
