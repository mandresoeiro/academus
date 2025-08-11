from rest_framework import permissions


class IsOwnerOnly(permissions.BasePermission):
    """
    Permite acesso somente ao proprietário do objeto (campo `user`).
    Retorna 403 se o usuário autenticado não for o dono.
    """

    message = "Você não tem permissão para acessar este recurso."

    def has_object_permission(self, request, view, obj):
        """
        Verifica se o campo `user` do objeto é igual ao usuário autenticado.
        Se o objeto não tiver `user`, retorna False silenciosamente.
        """
        return getattr(obj, "user", None) == request.user
