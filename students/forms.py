from django import forms
from .models import Student, StudentCampaign
from accounts.validators import allow_only_images_validator
from universities.models import University


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'university_id']
    
    # def __init__(self, *args, **kwargs):
    #     super(StudentForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         if field == 'student_id' or field == 'university_id':
    #             self.fields[field].widget.attrs['readonly'] = 'readonly'



class StudentCampaignForm(forms.ModelForm):
    student_credentials = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    class Meta:
        model = StudentCampaign
        fields = ['student_credentials', 'financial_need', 'campaign_message', 'payment_deadline']
    
    def __init__(self, *args, **kwargs):
        super(StudentCampaignForm, self).__init__(*args, **kwargs)
        
        self.fields['financial_need'].widget.attrs['placeholder'] = 'Amount Needed'
        self.fields['payment_deadline'].widget.attrs['placeholder'] = 'Deadline Date'
        
        

class AmountRaisedForm(forms.ModelForm):
    class Meta:
        model = StudentCampaign
        fields = ['amount_raised',]
