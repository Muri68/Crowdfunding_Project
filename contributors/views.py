from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.views import check_role_contributor
from accounts.forms import UserInfoForm, UserProfileForm
from accounts.models import UserProfile
from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
@user_passes_test(check_role_contributor)
def contributorDashboard(request):
    return render(request, 'contributors/contributorDashboard.html')



@login_required(login_url='login')
@user_passes_test(check_role_contributor)
def contributorProfile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserInfoForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('contributorProfile')
        else:
            print(profile_form.errors)
            print(user_form.errors)
            messages.error(request, profile_form.errors)
            messages.error(request, user_form.errors)
    else:
        profile_form = UserProfileForm(instance=profile)
        user_form = UserInfoForm(instance=request.user)

    context = {
        'profile_form': profile_form,
        'user_form' : user_form,
        'profile': profile,
    }
    return render(request, 'contributors/contributorProfile.html', context)
