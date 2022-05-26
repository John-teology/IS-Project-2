from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
import requests

from .models import *


# Create your views here.

def index(request):
    return render(request, "portfolio/index.html")



def leader(request):
    return render(request, "portfolio/leaderboards.html")



def read(request):
    x = requests.get('https://api.github.com/users/john-teology/repos')
    data = x.json()
    lang = []
    for i in range(len(data)):
        lang.append(data[i]['language'])
    return render(request, "portfolio/read.html", {
        'data' : lang
    })

    

