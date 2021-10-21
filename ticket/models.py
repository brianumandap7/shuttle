from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):        
    # required to associate Author model with User model (Important)
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255, blank=True, null = True)
    
    def __str__(self):
    	return str(self.status)

class Tickets(models.Model):        
    # required to associate Author model with User model (Important)
    ticket_id = models.AutoField(primary_key=True)
    start_date = models.DateField(blank=True, null = True)
    start_time = models.TimeField(blank=True, null = True)
    date_filed = models.DateTimeField(blank=True, null = True, auto_now_add=True)
    description = models.CharField(max_length=255, blank=True, null = True)
    email = models.CharField(max_length=255, blank=True, null = True)
    status = models.ForeignKey(Status, blank=True, null = True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
    	return str(self.description)+" Date Filed: "+str(self.date_filed)+" By: "+str(self.user)