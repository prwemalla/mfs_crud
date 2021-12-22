from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('task_service/', include('task_service.urls')),
    path('admin/', admin.site.urls),
]
