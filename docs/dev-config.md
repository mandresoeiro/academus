
# Ambiente de Desenvolvimento (Django)

## 🐣 Começando do Zero (Passo a Passo para Iniciantes)

### ✅ 1. Pré-requisitos
- Python 3.11+
- Node.js + npm
- Docker Desktop (opcional)
- PDM (gerenciador de dependências Python)

### 🖥️ 2. Clonar o projeto
```bash
git clone https://github.com/seu-usuario/academus.git
cd academus
```

### 📦 3. Instalar dependências Python
```bash
pdm install
```

### ⚙️ 4. Criar e configurar .env
```bash
cp .env.example .env
```

### 🐍 5. Rodar o backend
```bash
pdm run python backend/manage.py migrate
pdm run python backend/manage.py runserver
```

### 🌐 6. Rodar o frontend
```bash
cd frontend
npm install
npm run dev
```

### 👤 7. Criar superusuário
```bash
pdm run python backend/manage.py createsuperuser
```

---

## ✅ Sugestões (DevilLint)
- Corrigir `ORS_ALLOWED_ORIGINS` para `CORS_ALLOWED_ORIGINS`
- Usar adaptadores customizados do `allauth`
- Adicionar logging básico
- Usar `not DEBUG` para definir segurança de cookies

