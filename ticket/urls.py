from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'ticket'

urlpatterns = [
    path('', views.ticket, name='ticket-ticket'),
    path('file/', views.file, name='ticket-file'),
    path('record/', views.record, name='ticket-record'),
]


