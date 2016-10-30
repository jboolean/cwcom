from django.conf.urls import url
from . import views


app_name = 'base'
urlpatterns = [
	url(r'^past', views.PastView.as_view(), name='past'),
    url(r'^project/(?P<slug>[0-9A-Za-z\-_]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
    url(r'^system/(?P<slug>[0-9A-Za-z\-_]+)/$', views.SystemDetailView.as_view(), name='system-detail'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]