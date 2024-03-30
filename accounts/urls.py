from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.myAccount),
    path('registerContributor/', views.registerContributor, name='registerContributor'),
    # path('registerVendor/', views.registerVendor, name='registerVendor'),

    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),

]