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
    path('driver/', views.driver, name='exec-driver'),
    path('head/<int:tag>', views.headu, name='exec-head'),
    path('ftsu/<int:tag>', views.ftsu, name='exec-fts'),
    path('execu/<int:tag>', views.execu, name='exec-execu'),
]


