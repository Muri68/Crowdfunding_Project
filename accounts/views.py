from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import UserForm

# Create your views here.
def registerContributor(request):
    if request.method == 'POST':
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
            # mail_subject = 'Please activate your account'
            # email_template = 'accounts/emails/account_verification_email.html'
            # send_verification_email(request, user, mail_subject, email_template)
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