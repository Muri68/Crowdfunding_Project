from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'student_id', 'is_verified', 'created_at')
    list_display_links = ('full_name', 'user', 'student_id')
    list_editable = ('is_verified',)
    
admin.site.register(Student, StudentAdmin)