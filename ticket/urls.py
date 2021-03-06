from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'ticket'

urlpatterns = [
    path('', views.ticket, name='ticket-ticket'),
    path('file/', views.file, name='ticket-file'),
    path('record/', views.record, name='ticket-record'),
    path('dashtrack/', views.dashtrack, name='ticket-dashtrack'),
    path('track/', views.track, name='ticket-track'),
    path('shuttle_track/<int:tag>', views.shuttle_track, name='ticket-shuttle_track'),
    path('hdf', views.df, name = "hdf"),
    path('conf', views.conf, name = "conf"),
    path('admindash/', views.admindash, name = "admindash"),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)


