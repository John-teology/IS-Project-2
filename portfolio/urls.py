from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path('leaderboards/', views.leader, name="leader"),
    path('read/', views.read, name='read'),
    path('profileForm/', views.profileForm, name='profileForm'),
    path('formvalidation/', views.formValidation, name='checkform'),
    path('myprofile/', views.userProfile, name='profile'),

    
]