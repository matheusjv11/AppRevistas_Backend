"""BackendProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.urls import path
from django.contrib.auth import views as auth_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Snippets API",
#         default_version='v1',
#         description="Test description",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="contact@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    #path('api/', include('Revistas.urls')),
    # Endpoints para rest-auth https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html#social-media-authentication

    url(r'admin/', admin.site.urls),

    url(r'^api/', include("revistas.urls", namespace='revista-api')),

    url(r'^api/', include("artigos.urls", namespace='artigos-api')),

    url(r'^api/', include("noticias.urls", namespace='noticias-api')),

    url(r'^api/', include("usuarios.urls", namespace='usuarios-api')),

    # url(r'^swagger(?P<format>\.json|\.yaml)$',
    #     schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view.with_ui('swagger',
    #                                        cache_timeout=0), name='schema-swagger-ui'),
    # url(r'^redoc/$', schema_view.with_ui('redoc',
    #                                      cache_timeout=0), name='schema-redoc'),

    # Auth
    path('rest-auth/', include('rest_auth.urls')), path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset.html'), name='password_reset'),

    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
]

if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
