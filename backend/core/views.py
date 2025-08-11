# core/views.py
from django.urls.exceptions import NoReverseMatch
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class APIRootView(APIView):
    def get(self, request, *args, **kwargs):
        links = {}

        try:
            links["Perfil"] = reverse("accounts:me", request=request)
        except NoReverseMatch:
            links["Perfil"] = "URL 'accounts:me' não encontrada"

        try:
            links["Tarefas"] = reverse("dashboard:task-list", request=request)
        except NoReverseMatch:
            links["Tarefas"] = "URL 'dashboard:task-list' não encontrada"

        return Response(links, status=status.HTTP_200_OK)
