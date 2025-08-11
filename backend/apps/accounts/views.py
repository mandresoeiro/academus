from apps.accounts.serializers import UserReadSerializer, UserUpdateSerializer
from rest_framework import decorators, permissions, response, viewsets


class UserViewSet(viewsets.ViewSet):
    """
    Conjunto de endpoints relacionados ao usuário autenticado.

    Ações disponíveis:
    - GET /api/accounts/me/     → Consulta dados do usuário logado
    - PATCH /api/accounts/me/   → Atualiza parcialmente o próprio perfil
    """

    # 🔒 Apenas usuários autenticados podem acessar
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """
        Define o serializer a ser usado com base na requisição.
        """
        if self.action == "me":
            if self.request.method == "PATCH":
                return UserUpdateSerializer
            return UserReadSerializer
        return UserReadSerializer

    def list(self, request, *args, **kwargs):
        """
        GET /api/accounts/

        Endpoint desabilitado para listagem de usuários.
        Direciona para uso do /me/
        """
        return response.Response(
            {
                "detail": "Este endpoint não lista usuários. Use /me/ para acessar seu perfil."
            }
        )

    @decorators.action(
        detail=False,
        methods=["get", "patch"],
        permission_classes=[permissions.IsAuthenticated],
    )
    def me(self, request):
        """
        GET ou PATCH /api/accounts/me/

        Retorna ou atualiza os dados do próprio usuário autenticado.
        """
        user = request.user

        if request.method == "GET":
            serializer = self.get_serializer(user)
            return response.Response(serializer.data)

        # PATCH: atualização parcial do perfil
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)
