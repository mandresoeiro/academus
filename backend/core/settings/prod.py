# settings/prod.py

from .base import *

# 🚫 Modo produção: desativa debug
DEBUG = False

# 🌍 Hosts permitidos em produção
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=lambda v: v.split(","))

# 🛢️ Banco de dados PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    }
}

# ✉️ Configurações de e-mail com SMTP real
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool, default=True)
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")

# 🔒 Segurança recomendada para produção
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", cast=bool, default=True)

# 🔧 Ambiente identificado como produção
ENVIRONMENT = config("ENVIRONMENT", default="production")
