from django.contrib import admin
from .models import Student, StudentCampaign

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'student_id', 'is_verified', 'created_at')
    list_display_links = ('full_name', 'user', 'student_id')
    list_editable = ('is_verified',)
    

class CampaignAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'financial_need', 'amount_raised', 'payment_deadline', 'campaign_status', 'is_approve', 'created_at')
    list_display_links = ('full_name', 'user')
    
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentCampaign, CampaignAdmin)