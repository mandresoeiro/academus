import os

from django.core.wsgi import get_wsgi_application

# Lê a variável de ambiente DJANGO_ENV (padrão = dev)
env = os.environ.get("DJANGO_ENV", "dev")

# Define qual settings usar com base no ambiente
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"core.settings.{env}")

application = get_wsgi_application()
# Define o ambiente atual da aplicação
# Pode ser usado no código para mudar comportamentos.
