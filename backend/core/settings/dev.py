from .base import *

"""
🔧 Configurações de Desenvolvimento

Este arquivo herda do base.py e define ajustes específicos para o ambiente de desenvolvimento.
"""

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# SQLite para desenvolvimento local
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Email exibido no terminal
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "no-reply@localhost"

# Frontend local liberado
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]

# Ambiente atual
ENVIRONMENT = config("ENVIRONMENT", default="development")

SITE_ID = 1  # Necessário para dj-rest-auth + allauth funcionar corretamente
