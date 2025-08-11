"""
DevilKit Init Script - Setup profissional fullstack
Este script automatiza a criação de um projeto backend Django pronto para produção.

Autor: Marcio Soeiro
Licença: MIT
"""

from pathlib import Path

# Paths
root_dir = Path.cwd()
backend_dir = root_dir / "backend"
core_dir = backend_dir / "core"
settings_dir = core_dir / "settings"
apps_dir = backend_dir / "apps"
accounts_dir = apps_dir / "accounts"
requirements_dir = backend_dir / "requirements"
scripts_dir = backend_dir / "scripts"

# Estrutura de diretórios
dirs_to_create = [
    backend_dir,
    core_dir,
    settings_dir,
    apps_dir,
    accounts_dir,
    requirements_dir,
    scripts_dir,
]

# Arquivos base
files_to_create = {
    settings_dir / "__init__.py": "",
    settings_dir / "base.py": '"""Configurações base do Django."""\n',
    settings_dir / "dev.py": '"""Configurações de desenvolvimento."""\n',
    settings_dir / "prod.py": '"""Configurações de produção."""\n',
    backend_dir / ".env": "DEBUG=True\nSECRET_KEY=changeme\n",
    backend_dir / ".env.example": "DEBUG=True\nSECRET_KEY=changeme\n",
    backend_dir
    / "pytest.ini": "[pytest]\ndjango_find_project = false\npython_files = test_*.py\n",
    backend_dir
    / "README.md": "# Projeto DevilKit\n\nStack profissional com Django, React, Docker e mais.\n",
    backend_dir / "LICENSE": "MIT License\n\nCopyright (c) 2025 Marcio Soeiro\n",
    accounts_dir / "__init__.py": "",
    requirements_dir / "base.txt": "# Requisitos base\ndjango\npython-decouple\n",
    requirements_dir
    / "dev.txt": "# Requisitos de desenvolvimento\npytest\npytest-django\n",
    requirements_dir / "prod.txt": "# Requisitos de produção\ngunicorn\n",
    scripts_dir / "bootstrap.sh": "#!/bin/bash\necho 'Inicializando ambiente...'\n",
    backend_dir / ".dockerignore": "__pycache__/\n*.pyc\n.env\n",
    backend_dir / "test_smoke.py": "def test_smoke():\n    assert True\n",
}

# Criação de diretórios
for d in dirs_to_create:
    d.mkdir(parents=True, exist_ok=True)

# Criação de arquivos com conteúdo padrão
for file_path, content in files_to_create.items():
    file_path.write_text(content)

print("✅ Projeto backend DevilKit inicializado com sucesso!")
