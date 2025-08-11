# Endpoints - Módulo Dashboard (Exemplo)

## 📋 GET /api/dashboard/tasks/
Lista todas as tarefas.

**Resposta:**
```json
[
  {
    "id": 1,
    "title": "Revisar relatório",
    "status": "Pendente",
    "created_at": "2025-08-03T14:00:00Z"
  }
]
```

---

## ➕ POST /api/dashboard/tasks/
Cria uma nova tarefa.

**Exemplo de requisição:**
```json
{
  "title": "Nova tarefa",
  "description": "Escrever resumo técnico",
  "status": "Aberta"
}
```
