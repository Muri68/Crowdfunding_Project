from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'username', 'user_type', 'is_active')
    list_display_links = ('email', 'username', 'full_name')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)