from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# 📦 ENUM de Setores (departamentos responsáveis por tarefas)


# [BOAS PRÁTICAS] Avaliar se a lista de setores deveria vir de um modelo no banco (dinâmico) ou continuar fixa como ENUM.
class Sector(models.TextChoices):
    DIRECAO = "direcao", _("Direção")
    COORDENACAO = "coordenacao", _("Coordenação")
    DOCENCIA = "docencia", _("Docência")
    DADOS = "dados", _("Dados")
    DIAGRAMACAO = "diagramacao", _("Diagramação")
    PRODUCAO = "producao", _("Produção")
    COMUNICACAO = "comunicacao", _("Comunicação")


# 📦 ENUM de Status das Tarefas (etapas do fluxo de produção)
class TaskStatus(models.TextChoices):
    AGUARDANDO = "aguardando", "Aguardando"
    DIAGRAMANDO = "diagramando", "Diagramando"
    REVISAO = "revisao", "Revisão"
    AJUSTES = "ajustes", "Ajustes"
    APROVADA = "aprovada", "Aprovada"
    PRODUCAO = "producao", "Produção"


# ✅ MODELO PRINCIPAL: Tarefa no sistema
class Task(models.Model):
    sector = models.CharField(
        max_length=20, choices=Sector.choices, verbose_name="Setor Responsável"
    )
    title = models.CharField(max_length=255, verbose_name="Título")
    description = models.TextField(blank=True, verbose_name="Descrição")
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.AGUARDANDO,
        verbose_name="Status",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    is_done = models.BooleanField(default=False, verbose_name="Concluído")

    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ["-created_at"]

    def __str__(self):
        return f"[{self.get_sector_display()}] {self.title}"


# ✅ Modelo auxiliar opcional para cadastro de setores dinâmicos
class Setor(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


# ✅ Comentários vinculados a tarefas
class TaskComment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sector = models.CharField(max_length=20, choices=Sector.choices)
    content = models.TextField(verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentário de Tarefa"
        verbose_name_plural = "Comentários de Tarefas"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} ({self.get_sector_display()}): {self.content[:30]}"


# ✅ Sessão de Pomodoro com validação
# # class PomodoroSession(models.Model):
#     """
#     Sessão de Pomodoro relacionada a uma tarefa e um usuário.
#     """
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True)
#     start_time = models.DateTimeField(auto_now_add=True)

#     # Validação: mínimo 5 min (300s), máximo 2h (7200s)
#     duration_seconds = models.PositiveIntegerField(
#         default=1500,
#         validators=[
#             MinValueValidator(300),
#             MaxValueValidator(7200)
#         ]
#     )
#     paused_times = models.PositiveIntegerField(default=0)

#     class Meta:
#         verbose_name = "Sessão de Pomodoro"
#         verbose_name_plural = "Sessões de Pomodoro"
#         ordering = ['-start_time']

#     def __str__(self):
#         return f"{self.user} → {self.task} ({self.duration_seconds}s)"
