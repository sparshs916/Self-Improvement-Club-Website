from django.contrib import admin
from .models import ToDoList,Item,NewPost
# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(NewPost)

