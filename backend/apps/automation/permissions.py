from rest_framework.permissions import BasePermission


class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ("GET", "HEAD") or request.user.is_superuser
