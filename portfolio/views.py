from email import header
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


# https://avatars.githubusercontent.com/John-teology github profile image hehe
def read(request):
    try:
        headers = {"Authorization" : "Basic"}
        x = requests.get('https://api.github.com/users/John-teology/repos')
        data = x.json()
        lang = []
        for i in range(len(data)):
            lang.append(data[i]['name'])

        sum = []
        for a in lang:
            y = requests.get(f'https://api.github.com/repos/John-teology/{a}/languages')
            data1 = y.json()
            try:
                sum.append(data1['JavaScript'])  
            except KeyError:
                sum.append(0)  


        return render(request, "portfolio/read.html", {
            'lang': lang,
            'data' : sum
        })
    except KeyError:
        return render(request, "portfolio/read.html", {
            "msg": "try again later"
        })



# from bs4 import BeautifulSoup
# import requests

# x = requests.get('https://api.github.com/users/john-teology/repos')
# data = x.json()
# langu = []
# for i in range(len(data)):
#     langu.append(data[i]['name'])

# for la in langu:
#     html_text = requests.get(f'https://github.com/John-teology/{la}').content
#     soup = BeautifulSoup(html_text, 'lxml')
#     langs = soup.find_all('a',class_ = 'd-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3')
#     print(la)
#     for lang in langs:
#         d = lang.find_all('span')
#         for a in d:
#             print(a.text)
#     print('\n')
    






