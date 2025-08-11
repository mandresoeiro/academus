from apps.automation.serializers.generate import GenerateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class GenerateViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = GenerateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        prompt = serializer.validated_data["prompt"]
        tipo = serializer.validated_data["tipo"]
        generated_code = (
            f"# Código gerado para tipo '{tipo}':\n\nprint('Executando: {prompt}')"
        )
        return Response({"prompt": prompt, "tipo": tipo, "resultado": generated_code})
