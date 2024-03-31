from django.shortcuts import render
from universities.models import University


def home(request):
    universities = University.objects.all().order_by('-created_at')[:6]
    context = {
        'universities': universities
    }
    return render(request, 'home.html', context)