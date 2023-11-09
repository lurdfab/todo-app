from django.contrib import admin
from .models import *

# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date", "completed")
    # ordering = ["-date"]

admin.site.register(ToDo, ToDoAdmin)