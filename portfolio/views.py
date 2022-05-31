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
from bs4 import BeautifulSoup
import pandas as pd

from .models import *


# Create your views here.

def index(request):
    return render(request, "portfolio/index.html")



def leader(request):
    return render(request, "portfolio/leaderboards.html")
    

# https://avatars.githubusercontent.com/John-teology github profile image hehe
def read(request): 
    try:
        prog = []
        x = requests.get('https://api.github.com/users/John-teology/repos')
        data = x.json()
        langu = []
        for i in range(len(data)):
            langu.append(data[i]['name'])

        for la in langu:
            html_text = requests.get(f'https://github.com/John-teology/{la}').content
            soup = BeautifulSoup(html_text, 'lxml')
            langs = soup.find_all('a',class_ = 'd-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3')
            for lang in langs:
                d = lang.find_all('span')
                for a in d:
                    prog.append(a.text)
    

        return render(request, "portfolio/read.html", {
            'data' : prog
        })
    except KeyError:
        return render(request, "portfolio/read.html", {
            "msg": "try again later"
        })







def get_score(name,):
    # name = 'jaeam17'
    name = 'John-teology'

    x = requests.get(f'https://api.github.com/users/{name}/repos')
    data = x.json()
    prog = []
    langu = []
    lang_dict = {}
    for i in range(len(data)):
        langu.append(data[i]['name'])

    for la in langu:
        html_text = requests.get(f'https://github.com/{name}/{la}').content
        soup = BeautifulSoup(html_text, 'lxml')
        langs = soup.find_all('a',class_ = 'd-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3')
        for lang in langs:
            d = lang.find_all('span')
            for a in d:
                prog.append(a.text.replace("%",""))
        
        lang_dict[la] = {prog[i]: prog[i + 1] for i in range(0, len(prog), 2)}
        prog[:] = []


    df = pd.DataFrame(lang_dict)
    df.index.name = "languages"
    df = df.astype(float)
    df = df.reset_index(level=0)
    df = df.fillna(0)
    df['lang_score'] = df.sum(axis=1, numeric_only=True)


    into_db = { }

    dat = df['languages']

    for d in dat:
        val = df[df['languages'] == d ]['lang_score']
        into_db[d] = float(val.values)
        
    print(into_db)
    print(df['lang_score'].sum())


def test(request):
    input = { 'Python': 100, 'Java' :20, 'CSS':20,"hahah":43}
    saving(input)
    return HttpResponse('Success')
    
    
# def saving(input):
#     import re
#     try:
#         d = Leadtest(name = 'cd', **input)
#         d.save()
        
#     except TypeError as e:
#         s = str(e)
#         result = re.search("'(.*)'", s)
#         del input[result.group(1)]
#         saving(input)