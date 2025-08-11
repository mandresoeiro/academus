from apps.accounts.serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    View de login com JWT + dados do usuário na resposta.
    Substitui a view padrão do SimpleJWT.
    """

    serializer_class = CustomTokenObtainPairSerializer
