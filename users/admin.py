from django.contrib import admin
from .models import User

# Register your models here.



class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "email", "is_active", "date_joined")


admin.site.register(User, UserAdmin)