from django.urls import path, include
from . import views


urlpatterns = [
    path('studentDashboard/', views.studentDashboard, name='studentDashboard'),
    path('studentProfile/', views.studentProfile, name='studentProfile'),
]