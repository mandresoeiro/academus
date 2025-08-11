#!/usr/bin/env python
"""
🛠️ Script de entrada para tarefas administrativas do Django.
"""

import os
import sys


def main():
    """Executa comandos administrativos do Django com suporte a múltiplos ambientes."""

    # Define dinamicamente qual settings usar: dev, prod, etc
    env = os.environ.get("DJANGO_ENV", "dev")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"core.settings.{env}")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "⚠️ Não foi possível importar o Django. "
            "Verifique se o ambiente virtual está ativado e se o Django está instalado.\n\n"
            "💡 Dica: pip install -r requirements.txt"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
