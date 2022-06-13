from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path('profileform/', views.profileForm, name='profileForm'),
    path('formvalidation/', views.formValidation, name='checkform'),
    path('profile/<str:gitusername>', views.userProfile, name='profile'),
    path('refresh/<str:githubname>', views.refresh, name='refresh'),
    path('leaderboards/',views.leaderboard, name='leaderboard'),
    path('redirect/<int:userid>',views.redirect, name='redirect'),
    path('update/<str:gitname>',views.update_profile, name='update'),
    path('error',views.error, name='error'),

    
]