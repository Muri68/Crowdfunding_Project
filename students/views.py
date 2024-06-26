from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from accounts.views import check_role_student
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from .models import Student, StudentCampaign
from .forms import StudentForm, StudentCampaignForm
from donations.models import Donations


# Create your views here.
@login_required(login_url='login')
@user_passes_test(check_role_student)
def studentDashboard(request):
    student = get_object_or_404(Student, user=request.user)
    student_campaign = StudentCampaign.objects.filter(user=student).last()
    student_donation = Donations.objects.all()
    orders = Donations.objects.filter(students__in=[student.id]).order_by('-created_at')
    context = {
        'student_campaign': student_campaign,
        'student_donation': orders,
    }
    return render(request, 'students/studentDashboard.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_student)
def studentProfile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    student = get_object_or_404(Student, user=request.user)
    
    context = {
        'profile': profile,
        'student': student,
    }
    
    return render(request, 'students/studentProfile.html', context)

@login_required(login_url='login')
@user_passes_test(check_role_student)
def studentEditProfile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated Successfully.')
            return redirect('studentProfile')
        else:
            print(profile_form.errors)
            messages.error(request, profile_form.errors)
    else:
        profile_form = UserProfileForm(instance=profile)
    
    context = {
        'profile_form': profile_form,
        'profile': profile,
    }
    
    return render(request, 'students/studentEditProfile.html', context)



@login_required(login_url='login')
@user_passes_test(check_role_student)
def studentCampaign(request):
    student = get_object_or_404(Student, user=request.user)
    student_campaign = StudentCampaign.objects.filter(user=student).first()
    # student_campaign = StudentCampaign.objects.filter(students__in=[student.id]).first()
    # student_campaign = get_object_or_404(StudentCampaign, student=request.user)
    
    context = {
        'student_campaign': student_campaign,
        'student': student,
    }
    return render(request, 'students/studentCampaign.html', context)


@login_required(login_url='login')
@user_passes_test(check_role_student)
def studentCreateCampaign(request):
    student = get_object_or_404(Student, user=request.user)
    student_campaign = StudentCampaign.objects.filter(user=student)
    if student_campaign:
        messages.info(request, 'You already have a campaign. you cannot create another one')
        return redirect('studentCampaign')
    else:        
        if request.method == 'POST':
            form = StudentCampaignForm(request.POST, request.FILES)
            if form.is_valid():
                student_credentials = form.cleaned_data['student_credentials']
                financial_need = form.cleaned_data['financial_need']
                campaign_message = form.cleaned_data['campaign_message']
                payment_deadline = form.cleaned_data['payment_deadline']
                campaign = StudentCampaign.objects.create(user=student, student_credentials=student_credentials, financial_need=financial_need, campaign_message=campaign_message, payment_deadline=payment_deadline)
                campaign.save()
                messages.success(request, 'Campaign created Successfully.')
                return redirect('studentCampaign')
            else:
                print(form.errors)
                messages.error(request, form.errors)
        else:
            form = StudentCampaignForm()
    
    context = {
        'form': form,
    }
    return render(request, 'students/studentCreateCampaign.html', context)