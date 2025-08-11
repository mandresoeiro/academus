from apps.dashboard.models import Sector  # ✅ Importação correta
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleChoices(models.TextChoices):
    """
    Enumeração dos papéis possíveis de um usuário no sistema.

    Opções:
        - ADMIN: Administrador
        - STUDENT: Aluno
        - DOCENCIA: Docente
    """

    ADMIN = "admin", "Administrador"
    STUDENT = "student", "Aluno"
    DOCENCIA = "docencia", "Docência"


class User(AbstractUser):
    """
    Modelo customizado de usuário do sistema Academus.

    Extende o AbstractUser padrão do Django para incluir:
    - Função (`role`): Aluno, Docente ou Administrador.
    - Setor (`sector`): Setor institucional ao qual o usuário pertence.

    Campos herdados:
        - username, email, first_name, last_name, password, etc.

    Campos adicionados:
        role (str): Define o papel do usuário no sistema.
        sector (str): Define o setor do usuário (coordenação, produção, etc.).
    """

    role = models.CharField(
        max_length=20,
        choices=[(role.value, role.name.title()) for role in RoleChoices],
        default=RoleChoices.STUDENT,
        verbose_name=_("Função"),
        help_text=_("Define o papel do usuário no sistema."),
    )

    sector = models.CharField(
        max_length=20,
        choices=Sector.choices,
        default=Sector.COORDENACAO,
        verbose_name=_("Setor do Usuário"),
        help_text=_("Define o setor ao qual o usuário pertence."),
    )

    def __str__(self):
        return (
            f"{self.username} ({self.get_role_display()} - {self.get_sector_display()})"
        )
