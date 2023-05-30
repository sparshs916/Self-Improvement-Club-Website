from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # links model to built in user model
    profileImage = models.ImageField(upload_to='profile_pics/', null=True, blank=True) 
  #adding profile 

