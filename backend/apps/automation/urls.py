from apps.automation.views.generate import GenerateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("generate", GenerateViewSet, basename="generate")

urlpatterns = router.urls
