from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .utils import detectUser, send_verification_email
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .models import User, UserProfile
from .forms import UserForm
from students.forms import StudentForm



# Restrict the vendor from accessing the customer page
def check_role_student(user):
    if user.user_type == 1:
        return True
    else:
        raise PermissionDenied


# Restrict the customer from accessing the vendor page
def check_role_contributor(user):
    if user.user_type == 2:
        return True
    else:
        raise PermissionDenied


# Create your views here.
def registerContributor(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            ######### Create the user using create_user method #########
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.user_type = User.CONTRIBUTOR
            user.save()

            ########## Send verification email ##########
            mail_subject = 'Please activate your account'
            email_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, email_template)
            messages.success(request, 'Your account has been registered successfully!')
            return redirect('registerContributor')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerContributor.html', context)



def registerStudent(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        # store the data and create the user
        form = UserForm(request.POST)
        s_form = StudentForm(request.POST, request.FILES)
        if form.is_valid() and s_form.is_valid:
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.user_type = User.STUDENT
            user.save()
            student = s_form.save(commit=False)
            student.user = user
            student_id = s_form.cleaned_data['student_id']
            university_id = s_form.cleaned_data['university_id']
            user_profile = UserProfile.objects.get(user=user)
            student.user_profile = user_profile
            student.save()

            # Send verification email
            # mail_subject = 'Please activate your account'
            # email_template = 'accounts/emails/account_verification_email.html'
            # send_verification_email(request, user, mail_subject, email_template)

            messages.success(request, 'Your account has been registered successfully! Please wait for the approval.')
            return redirect('registerStudent')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
        s_form = StudentForm()

    context = {
        'form': form,
        's_form': s_form,
    }

    return render(request, 'accounts/registerStudent.html', context)



def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('myAccount')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('login')



@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)


@login_required(login_url='login')
@user_passes_test(check_role_contributor)
def contributorDashboard(request):
    return render(request, 'accounts/contributorDashboard.html')


@login_required(login_url='login')
@user_passes_test(check_role_student)
def studentDashboard(request):
    return render(request, 'accounts/studentDashboard.html')



def activate(request, uidb64, token):
    # Activate the user by setting the is_active status to True
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulation! Your account is activated.')
        return redirect('myAccount')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('myAccount')