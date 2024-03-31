from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.myAccount),
    path('registerContributor/', views.registerContributor, name='registerContributor'),
    path('registerStudent/', views.registerStudent, name='registerStudent'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('myAccount/', views.myAccount, name='myAccount'),
    path('contributorDashboard/', views.contributorDashboard, name='contributorDashboard'),
    path('studentDashboard/', views.studentDashboard, name='studentDashboard'),
    
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

]