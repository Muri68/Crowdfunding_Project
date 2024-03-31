from django.contrib import admin
from .models import University

# Register your models here.thumbnail
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'university_name', 'short_name', 'created_at')
    list_display_links = ('university_name',)
    # list_editable = ('is_approved',)
    
admin.site.register(University, UniversityAdmin)