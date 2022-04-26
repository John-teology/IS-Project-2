from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount

from .models import *

# Create your views here.
@login_required
def index(request):
    data = SocialAccount.objects.get(user=request.user).extra_data
    return render(request, "portfolio/index.html",{
        'data' : data['login']
    })

