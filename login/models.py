from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Roles(models.Model):
	role_id = models.AutoField(primary_key=True)
	role = models.CharField(max_length=255, blank=True, null = True)

	def __str__(self):
		return self.role

class Author(models.Model):        
    # required to associate Author model with User model (Important)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)


    # additional fields
   
    role = models.ForeignKey(Roles, default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(blank=True, null = True, upload_to ='uploads/')

    def __str__(self):
        return self.user.username