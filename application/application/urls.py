"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.models import LogEntry

urlpatterns = [
    path('client/', include('client.urls')),
    path('human-resource/', include('human_resource.urls')),
    path('about-us/', include('about_us.urls')),
    path('bulletin/', include('bulletin.urls')),
    path('panda/', include('panda.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Legacy Law Admin"
admin.site.site_title = "Legacy Law Admin Portal"
admin.site.index_title = "Welcome to Legacy Law Admin Portal"

LogEntry.objects.all().delete()
