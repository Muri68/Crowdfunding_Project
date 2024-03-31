from django.db import models
from accounts.models import User, UserProfile
from universities.models import University

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
    student_id = models.CharField(max_length=50)
    university_id = models.ForeignKey(University, on_delete=models.CASCADE, related_name='student_university')
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        
     # Add helper function for Admin display 
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

    def __str__(self):
        return self.user.email


# class StudentCampaign(models.Model):
#     CAMPAIGN_STATUS = (
#         ('Completed', 'Completed'),
#         ('Ongoing', 'Ongoing'),
#         ('Cancelled', 'Cancelled'),
#     )
    
#     user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
#     user_profile = models.OneToOneField(UserProfile, related_name='userprofile', on_delete=models.CASCADE)
#     student_credentials = models.ImageField(upload_to='student/credentials')
#     financial_need = models.DecimalField(max_digits=10, decimal_places=2)
#     campaign_status = models.CharField(max_length=15, choices=CAMPAIGN_STATUS, default='Ongoing')
    