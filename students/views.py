from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.views import check_role_student

# Create your views here.
@login_required(login_url='login')
@user_passes_test(check_role_student)
def studentDashboard(request):
    return render(request, 'students/studentDashboard.html')



@login_required(login_url='login')
@user_passes_test(check_role_student)
def studentProfile(request):
    return render(request, 'students/studentProfile.html')