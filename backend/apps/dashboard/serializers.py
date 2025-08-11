from rest_framework import serializers

from .models import Setor, Task, TaskComment

# from .models import PomodoroSession  # ⛔ Desativado temporariamente


# ✅ TAREFAS
class TaskSerializer(serializers.ModelSerializer):
    """
    Serializador para Tarefa com exibição do nome do setor.
    """

    sector_display = serializers.CharField(source="get_sector_display", read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")


# ✅ SETORES (modelo auxiliar)
class SetorSerializer(serializers.ModelSerializer):
    """
    Serializador do modelo auxiliar Setor.
    """

    class Meta:
        model = Setor
        fields = "__all__"


# ⛔ POMODORO DESATIVADO
# class PomodoroSessionSerializer(serializers.ModelSerializer):
#     """
#     Serializador para Sessão de Pomodoro com:
#     - task_id (entrada, write-only)
#     - task (detalhado, read-only)
#     - validações integradas
#     """
#     task = TaskSerializer(read_only=True)
#     task_id = serializers.PrimaryKeyRelatedField(
#         queryset=Task.objects.all(),
#         source='task',
#         write_only=True
#     )
#
#     class Meta:
#         model = PomodoroSession
#         fields = [
#             'id',
#             'user',
#             'task',
#             'task_id',
#             'start_time',
#             'duration_seconds',
#             'paused_times'
#         ]
#         read_only_fields = ['user', 'start_time']
#
#     def validate_duration_seconds(self, value):
#         """
#         Validação extra para garantir tempo coerente,
#         mesmo com os validators no model.
#         """
#         if value < 300:
#             raise serializers.ValidationError("Duração mínima é 5 minutos (300s).")
#         if value > 7200:
#             raise serializers.ValidationError("Duração máxima é 2 horas (7200s).")
#         return value


# ✅ COMENTÁRIOS
class TaskCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # nome do usuário
    sector = serializers.CharField(source="get_sector_display", read_only=True)

    class Meta:
        model = TaskComment
        fields = ["id", "task", "user", "sector", "content", "created_at"]
        read_only_fields = ["id", "created_at", "user", "sector", "task"]
