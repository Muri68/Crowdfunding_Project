from django import forms
from .models import Student
from accounts.validators import allow_only_images_validator
from universities.models import University


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'university_id']
        widgets = {
        'university_id': forms.Select(attrs={'class': 'form-control contact-form__input-box'}),
    }
    



