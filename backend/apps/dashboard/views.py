from django.conf import settings
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Setor, Task, TaskComment
from .serializers import (  # PomodoroSessionSerializer  # ⛔ Desativado temporariamente
    SetorSerializer, TaskCommentSerializer, TaskSerializer)

# from .models import PomodoroSession  # ⛔ Desativado temporariamente




# ✅ Tarefas
class TaskViewSet(viewsets.ModelViewSet):
    """
    API de Tarefas:
    - Listar todas as tarefas
    - Criar novas tarefas
    - Filtrar por setor via ?sector=nome
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        sector = self.request.query_params.get("sector")
        if sector:
            return self.queryset.filter(sector=sector)
        return self.queryset


# ✅ Setores (modelo auxiliar)
class SetorViewSet(viewsets.ModelViewSet):
    """
    API para CRUD do modelo Setor (cadastro auxiliar livre).
    """

    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
    permission_classes = [IsAuthenticated]


# ✅ Comentários por tarefa
class TaskCommentListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs["task_id"]
        return TaskComment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs["task_id"]
        task = Task.objects.get(pk=task_id)
        serializer.save(
            user=self.request.user,
            task=task,
            sector=self.request.user.sector,  # ajuste se o model de usuário for diferente
        )


# ✅ Dashboards por setor
class DocenciaDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"mensagem": "Bem-vindo ao painel de Docência!"})


class ProducaoDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"mensagem": "Bem-vindo ao painel da Produção!"})


# ⛔ Sessões de Pomodoro (temporariamente desativadas)
# class PomodoroSessionViewSet(viewsets.ModelViewSet):
#     queryset = PomodoroSession.objects.all()
#     serializer_class = PomodoroSessionSerializer
#     permission_classes = [IsAuthenticated, IsOwnerOnly]
#
#     def get_queryset(self):
#         return PomodoroSession.objects.filter(user=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# ✅ Diagnóstico de ambiente
@api_view(["GET"])
def ambiente_view(request):
    """
    Retorna o ambiente atual da aplicação (ex: development, production).
    Útil para ajustes no frontend.
    """
    return Response({"ambiente": settings.ENVIRONMENT})
