from django.contrib import admin

from .models import Status, Tickets, Stations, shuttle, destination, current_loc
# Register your models here.
admin.site.register(Status)
admin.site.register(Tickets)
admin.site.register(Stations)
admin.site.register(shuttle)
admin.site.register(destination)
admin.site.register(current_loc)
