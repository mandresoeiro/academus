from apps.dashboard.models import Task, TaskStatus
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=Task)
def log_task_created_or_updated(sender, instance, created, **kwargs):
    """
    📝 Sinal chamado quando uma Tarefa é criada ou atualizada.
    """
    if created:
        print(f"📌 Nova tarefa criada: {instance.title}")
    else:
        print(f"✏️ Tarefa atualizada: {instance.title}")


@receiver(pre_save, sender=Task)
def check_task_before_save(sender, instance, **kwargs):
    """
    ⏳ Verificação antes de salvar a tarefa.
    Define 'aguardando' se o status estiver vazio (evita erro de coerência).
    """
    if not instance.status:
        instance.status = TaskStatus.AGUARDANDO
