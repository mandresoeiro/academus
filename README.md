# 🚀 DevilKit Stack – Setup Profissional Django + React

[![GitHub License](https://img.shields.io/github/license/mandresoeiro/devilkit-stack?color=blue)](https://github.com/mandresoeiro/devilkit-stack/blob/main/LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/mandresoeiro/devilkit-stack/actions)
[![Made with PDM](https://img.shields.io/badge/pdm-enabled-blue)](https://pdm.fming.dev)

> **DevilKit** é um projeto base com estrutura profissional para iniciar aplicações fullstack usando **Django** no backend e **React** no frontend. Automatize tudo com uma CLI poderosa usando [Typer](https://typer.tiangolo.com/).

---

## 📦 Estrutura

```text
devilkit-stack/
├── src/devilkit/         # Código da CLI com Typer
├── backend/              # Projeto Django (gerado pelo comando init)
├── tests/                # Testes automatizados
├── pyproject.toml        # Configuração PDM + Typer
├── devilkit.py           # Entry point da CLI
└── README.md             # Este arquivo
```

---

## ⚙️ Instalação

```bash
git clone https://github.com/mandresoeiro/devilkit-stack.git
cd devilkit-stack
pdm install
```

---

## 🚀 Uso da CLI

Crie a estrutura base do backend com:

```bash
pdm run devilkit init backend
```

Você pode alterar o nome:

```bash
pdm run devilkit init nome-do-projeto
```

---

## 🧪 Rodando os testes

```bash
pytest
```

---

## 📂 Tecnologias e ferramentas

- [x] Python 3.11+
- [x] [Typer](https://typer.tiangolo.com/)
- [x] [PDM](https://pdm.fming.dev)
- [x] Docker (opcional)
- [x] Estrutura pensada para produtividade e organização

---

## 🤝 Contribuindo

Pull requests são bem-vindos. Para mudanças maiores, abra uma issue antes de modificar o que já existe.

---

## 📄 Licença

Distribuído sob a licença **MIT**. Veja `LICENSE` para mais informações.
