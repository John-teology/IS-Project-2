from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path("register",views.register, name="register"),
    path("login",views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path('social-auth', include('social_django.urls', namespace='social')),

    
]