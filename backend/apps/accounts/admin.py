from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Admin customizado para o modelo User.
    Adiciona os campos 'role' e 'sector' ao painel de administração.
    """

    # 📌 Campos exibidos na listagem de usuários
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "sector",  # novos campos
        "is_active",
        "is_staff",
    )

    # 🔍 Campos que podem ser pesquisados
    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )

    # 🔒 Campos somente leitura
    readonly_fields = ("last_login", "date_joined")

    # 🧮 Filtros laterais
    list_filter = (
        "role",
        "sector",
        "is_active",
        "is_staff",
        "is_superuser",
    )

    # 🔠 Ordenação padrão da listagem
    ordering = ("username",)

    # 🧾 Campos exibidos no formulário de edição
    fieldsets = BaseUserAdmin.fieldsets + (
        (
            "Informações Acadêmicas",
            {
                "fields": ("role", "sector"),
            },
        ),
    )

    # 🆕 Campos exibidos ao adicionar novo usuário
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (
            "Informações Acadêmicas",
            {
                "fields": ("role", "sector"),
            },
        ),
    )
