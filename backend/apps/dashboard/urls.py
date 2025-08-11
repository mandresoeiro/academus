from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (  # PomodoroSessionViewSet,  # ⛔ Temporariamente desativado
    DocenciaDashboardView, ProducaoDashboardView, SetorViewSet,
    TaskCommentListCreateView, TaskViewSet)

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)
router.register(r"setores", SetorViewSet)
# router.register(r'pomodoro-sessions', PomodoroSessionViewSet)  # ⛔ Oculto por enquanto

app_name = "dashboard"

urlpatterns = [
    path("", include(router.urls)),
    # Dashboards por setor
    path(
        "painel/docencia/", DocenciaDashboardView.as_view(), name="docencia-dashboard"
    ),
    path(
        "painel/producao/", ProducaoDashboardView.as_view(), name="producao-dashboard"
    ),
    # Comentários por tarefa
    path(
        "tasks/<int:task_id>/comments/",
        TaskCommentListCreateView.as_view(),
        name="task-comments",
    ),
]
