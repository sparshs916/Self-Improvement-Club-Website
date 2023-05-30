from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class NewPost(models.Model):
    textfield = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True) #will save timestamp of current time each time object saved
    dateCreated = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.textfield
