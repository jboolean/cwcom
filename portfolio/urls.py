"""cw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^admin/clearcache/', include('clearcache.urls')),
    re_path(r'^admin/', admin.site.urls),
	re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^s3upload/', include('s3upload.urls')),
    re_path(r'^', include('base.urls', namespace='base')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)