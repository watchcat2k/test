from django.contrib import admin
from . import models

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_username', 'user_password', 'user_name', 'user_avatar')
    
admin.site.register(models.User, UserAdmin)