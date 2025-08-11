# Endpoints - Módulo Accounts (Autenticação JWT)

## 🔐 POST /api/token/
Autentica o usuário e retorna os tokens de acesso e refresh.

**Corpo da requisição:**
```json
{
  "username": "usuario",
  "password": "senha"
}
```

**Resposta:**
```json
{
  "access": "<token JWT>",
  "refresh": "<token Refresh>"
}
```

---

## 🔁 POST /api/token/refresh/
Renova o token de acesso com o token de refresh.

**Corpo da requisição:**
```json
{
  "refresh": "<token Refresh>"
}
```

**Resposta:**
```json
{
  "access": "<novo token JWT>"
}
```

---

## ✅ POST /api/token/verify/
Verifica se um token JWT ainda é válido.

**Corpo da requisição:**
```json
{
  "token": "<token JWT>"
}
```

**Resposta:**
```json
{}
```
