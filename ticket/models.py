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

class easy_maps(models.Model):        
    # required to associate Author model with User model (Important)
    address = models.CharField(max_length=255, blank=True, null = True)
    
    def __str__(self):
        return str(self.address)

class shuttle(models.Model):        
    # required to associate Author model with User model (Important)
    shuttle = models.CharField(max_length=255, blank=True, null = True)
    driver = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.shuttle)+" "+str(self.driver)

class destination(models.Model):        
    # required to associate Author model with User model (Important)
    destination = models.CharField(max_length=255, blank=True, null = True)
    
    def __str__(self):
        return str(self.destination)

class current_loc(models.Model):        
    # required to associate Author model with User model (Important)
    current_loc = models.CharField(max_length=255, blank=True, null = True)
    
    def __str__(self):
        return str(self.current_loc)

class Stations(models.Model):
    station_id = models.AutoField(primary_key=True)
    longlat = models.CharField(max_length=255, blank=True, null = True)
    current_loc = models.ForeignKey(current_loc, null=True, blank=True, on_delete=models.CASCADE)
    destination = models.ForeignKey(destination, null=True, blank=True, on_delete=models.CASCADE)
    shuttle = models.ForeignKey(shuttle, null=True, blank=True, on_delete=models.CASCADE)

    a_driver = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.shuttle)+" "+str(self.current_loc)+" "+str(self.a_driver)