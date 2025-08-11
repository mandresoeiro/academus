import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
def test_generate_endpoint_authenticated():
    user = User.objects.create_user(username="test", password="1234")
    client = APIClient()
    client.login(username="test", password="1234")
    response = client.post(
        "/api/generate/", {"prompt": "Criar API de tarefas", "tipo": "view"}
    )
    assert response.status_code == 200
    assert "resultado" in response.data
