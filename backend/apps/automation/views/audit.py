from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AuditView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        code = request.data.get("code", "")
        feedback = f"Análise simulada do código: {code[:30]}..."
        return Response({"feedback": feedback})
