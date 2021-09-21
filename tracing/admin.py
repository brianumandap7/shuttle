from django.contrib import admin

from .models import Contact_tracing, fever, cold, body_pain, loss_of_taste, loss_of_smell, headache
# Register your models here.
admin.site.register(Contact_tracing)
admin.site.register(fever)
admin.site.register(cold)
admin.site.register(body_pain)
admin.site.register(loss_of_smell)
admin.site.register(loss_of_taste)
admin.site.register(headache)