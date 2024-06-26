from django.db import models
from accounts.models import User, UserProfile
from universities.models import University
from datetime import date

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


class StudentCampaign(models.Model):
    CAMPAIGN_STATUS = (
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    
    user = models.ForeignKey(Student, related_name='campaign_student', on_delete=models.CASCADE)
    student_credentials = models.ImageField(upload_to='student/credentials')
    financial_need = models.DecimalField(max_digits=10, decimal_places=2)
    amount_raised = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    campaign_message = models.TextField()
    campaign_status = models.CharField(max_length=15, choices=CAMPAIGN_STATUS, default='Ongoing')
    payment_deadline = models.DateField()
    is_approve = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Student Campaign'
        verbose_name_plural = 'Student Campaigns'
        
    # Add helper function for Admin display 
    def full_name(self):
        return f'{self.user.user.first_name} {self.user.user.last_name}'
    
    @property
    def days_remaining(self):
        today = date.today()
        remaining = self.payment_deadline.date() - today
        return remaining
    

    def __str__(self):
        return f'{self.user.user.first_name} {self.user.user.last_name}'
    