# apps/accounts/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

app_name = "apps.accounts"

router = DefaultRouter()
router.register(r"", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("me/", UserViewSet.as_view({"get": "me"}), name="me"),
]
