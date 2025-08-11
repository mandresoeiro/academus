from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


# 🔐 SERIALIZER DE LOGIN COM JWT + DADOS DO USUÁRIO
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer customizado para autenticação JWT.
    Retorna os tokens e os dados do usuário autenticado.
    """

    def validate(self, attrs):
        # ⚙️ Executa a validação padrão (gera tokens)
        data = super().validate(attrs)

        # 👤 Inclui dados personalizados do usuário autenticado
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "role": self.user.role,
            "sector": self.user.sector,
        }

        return data


# 📘 SERIALIZER DE LEITURA DO PERFIL
class UserReadSerializer(serializers.ModelSerializer):
    """
    Serializer somente leitura dos dados do usuário.
    Usado em endpoints como /me/
    """

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "role",
            "sector",
            "is_active",
            "is_staff",
        ]
        read_only_fields = fields


# ✏️ SERIALIZER DE ATUALIZAÇÃO PARCIAL DO PERFIL
class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Permite atualizar nome e username do próprio perfil.
    Campos como senha, role e setor não podem ser alterados aqui.
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]
