from django.contrib import admin

from .models import Status, Tickets, Stations, shuttle, destination, current_loc, imhere, tracing, answers, questions, hdf, reserve
# Register your models here.
admin.site.register(Status)
admin.site.register(Tickets)
admin.site.register(Stations)
admin.site.register(shuttle)
admin.site.register(destination)
admin.site.register(current_loc)
admin.site.register(imhere)
admin.site.register(tracing)
admin.site.register(answers)
admin.site.register(questions)
admin.site.register(hdf)
admin.site.register(reserve)