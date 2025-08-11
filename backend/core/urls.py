# 🌐 View raiz da API
from core.views import APIRootView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# 📘 Documentação automática com drf-spectacular
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
# 🔐 Autenticação com JWT (para uso manual ou fallback)
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    # 🔧 Painel administrativo do Django
    path("admin/", admin.site.urls),
    # 🔐 Autenticação com JWT (opcional)
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # ✅ Autenticação completa com dj-rest-auth
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/registration/", include("dj_rest_auth.registration.urls")),
    # 📁 Rotas por app
    path("api/accounts/", include("apps.accounts.urls", namespace="accounts")),
    path("api/dashboard/", include("apps.dashboard.urls", namespace="dashboard")),
    # 🌍 Raiz da API com links úteis
    path("", APIRootView.as_view()),
    # 📚 Documentação OpenAPI
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]

# 🗂️ Arquivos de mídia no modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
