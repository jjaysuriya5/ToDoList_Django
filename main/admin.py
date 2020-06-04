from django.contrib import admin

# Register your models here.

from .models import ToDoList, List

admin.site.register(ToDoList)
admin.site.register(List)