from authapi import views
from authapi.utils.handlers import view_404_exception
from django.conf.urls import handler404
from django.urls import include, path, re_path
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Authentication API",
      default_version='v0.1.0',
      description="Public django API for user management and authentication based on JWT",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("", views.api_root, name="home"),
    # endpoints from Django REST framework JWT package
    path('auth/', include('authapi.urls')),
    re_path(r'^schema(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^schema/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

handler404 = view_404_exception
