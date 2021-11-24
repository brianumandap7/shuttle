from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'fts'

urlpatterns = [
    path('', views.fts, name='fts-fts'),
    path('head/', views.head, name='head-head'),
    path('exec/', views.exec, name='exec-exec'),
    path('head/<int:tag>', views.headu, name='exec-head'),
]


