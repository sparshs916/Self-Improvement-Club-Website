from django.contrib import admin
from .models import NewPost
from register.models import UserProfile
# Register your models here.

admin.site.register(NewPost)
admin.site.register(UserProfile)

