from django.contrib import admin
from .models import User, Profile

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'user', 'phone']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)