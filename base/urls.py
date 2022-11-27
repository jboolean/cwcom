from django.urls import re_path
from . import views


app_name = 'base'
urlpatterns = [
  re_path(r'^past', views.PastView.as_view(), name='past'),
  re_path(r'^project/(?P<slug>[0-9A-Za-z\-_]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
  re_path(r'^system/(?P<slug>[0-9A-Za-z\-_]+)/$', views.SystemDetailView.as_view(), name='system-detail'),
  re_path(r'^(?P<slug>[0-9A-Za-z\-_]+)/$', views.PortfolioView.as_view(), name='portfolio'),
  re_path(r'^$', views.PortfolioView.as_view(), name='index',  kwargs=dict(slug='portfolio'))
]