from django.shortcuts import render
from universities.models import University
from accounts.models import User
from students.models import Student


def home(request):
    universities = University.objects.all().order_by('-created_at')[:6]
    students = Student.objects.all()
    context = {
        'universities': universities,
        'students': students,
    }
    return render(request, 'home.html', context)



def aboutUs(request):
    return render(request, 'about.html')


def contactUs(request):
    return render(request, 'contactUs.html')