from django.core.exceptions import FieldError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

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







def get_score(githubName,user,course_id,yearlevel_id):
    x = requests.get(f'https://api.github.com/users/{githubName}/repos')
    data = x.json()
    prog = []
    projects = []
    lang_dict = {}
    for i in range(len(data)):
        projects.append(data[i]['name'])

    for project in projects:
        html_text = requests.get(f'https://github.com/{githubName}/{project}').content
        soup = BeautifulSoup(html_text, 'lxml')
        languages = soup.find_all('a',class_ = 'd-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3')
        for lang in languages:
            d = lang.find_all('span')
            for a in d:
                prog.append(a.text.replace("%",""))
        # list to dictionary
        lang_dict[project] = {prog[i]: prog[i + 1] for i in range(0, len(prog), 2)}
        prog[:] = []
    # dictionary to dataframe
    df = pd.DataFrame(lang_dict)
    df.index.name = "languages"
    df = df.astype(float)
    df = df.reset_index(level=0)
    df = df.fillna(0)
    df['lang_score'] = df.sum(axis=1, numeric_only=True)


    into_db = { }

    for d in df['languages']:
        val = df[df['languages'] == d ]['lang_score']
        into_db[d] = float(val.values)
    
  

    for key in list(into_db.keys()):
        if key == '1C Enterprise':
            into_db['CEnterprise'] = into_db.pop(key)
        if key == 'ASP.NET':
            into_db['ASPNET'] = into_db.pop(key)
        if key == 'C#':
            into_db['CSharp'] = into_db.pop(key)
        if key == 'C++':
            into_db['Cplus'] = into_db.pop(key)
        if key == 'F#':
            into_db['FSharp'] = into_db.pop(key)
        if key == 'HTML+RAZOR':
            into_db['HTML_Razor'] = into_db.pop(key)
        if key == 'Jupyter Notebook':
            into_db['JupyterNotebook'] = into_db.pop(key)
        if key == 'Objective-C':
            into_db['ObjectiveC'] = into_db.pop(key)
        if key == 'Objective-C++':
            into_db['ObjectiveCplus'] = into_db.pop(key)
        if key == 'OpenEdge ABL':
            into_db['OpenEdgeABL'] = into_db.pop(key)
        if key == 'Perl 6':
            into_db['Perl6'] = into_db.pop(key)
        if key == 'Protocol Buffer':
            into_db['ProtocolBuffer'] = into_db.pop(key)

    into_db['userID'] = user
    into_db['courseID'] = course_id
    into_db['yearID'] = yearlevel_id
    into_db['overallScore'] = df['lang_score'].sum()

    saving(into_db,user)

    
    
def saving(input,user):
    try:
        if (LeaderBoards.objects.filter(userID=user).count() > 0):
            LeaderBoards.objects.get(userID=user).delete()
            newlead = LeaderBoards(**input)
            newlead.save()

        else:
            d = LeaderBoards(**input)
            d.save()
        
    except TypeError as e:
        s = str(e)
        result = re.search("'(.*)'", s)
        del input[result.group(1)]
        saving(input,user)


@login_required
def profileForm(request):
    userid = User.objects.get(username = request.user)
    if (Profile.objects.filter(userID = userid).count() > 0):
        p = Profile.objects.get(userID = request.user)
        return HttpResponseRedirect(reverse('profile', args=(str(p.githubName),)))
    
    yearlev = YearLevel.objects.all()
    course = Course.objects.all()
    return render(request,"portfolio/userForm.html",{
        'yearlevels': yearlev,
        'courses' : course,
    })

def formValidation(request):
    user = request.user
    if request.method == "POST":
        c_id = request.POST['courseid']
        yl_id = request.POST['yearlevelid']
        nickname = request.POST['nickname']
        githubName = request.POST['github']
        about = request.POST['aboutMe']
    if is_githubvalid(githubName) == 0:
        request.session['githuberr'] = 'not valid Github Name'
        request.session['githubn'] = githubName
        return HttpResponseRedirect(reverse('profileForm'))
    if is_githubnameExist(githubName.lower()):
        request.session['githubexist'] = "The Github username is already exist"
        request.session['githubn'] = githubName
        return HttpResponseRedirect(reverse('profileForm'))

    else:
        course_id = Course.objects.get(pk = c_id)
        yearlevel_id = YearLevel.objects.get(pk = yl_id)
        userprof = Profile(userID = user,nickname = nickname, githubName = githubName.lower(), aboutMe = about)
        userprof.save()
        get_score(githubName,user,course_id,yearlevel_id)
        try:
            del request.session['githuberr']
            del request.session['githubexist']
            del request.session['githubn']
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('profile', args=(str(userprof.githubName),)))
    

def is_githubvalid(githubName):
    x = requests.get(f'https://github.com/{githubName}').status_code
    if x == 200:
        return True
    else:
        return False
    
def is_githubnameExist(githubName):
    if (Profile.objects.filter(githubName = githubName).count() > 0):
        return True
    else:
        return False
    


def userProfile(request,gitusername):
    
    profile = Profile.objects.get(githubName = gitusername)
    d = profile.userID
    user = User.objects.get(username = d)
    user_P = LeaderBoards.objects.get(userID = d)
    lang_percentage = get_lang_rank(gitusername)
    return render(request, 'portfolio/profile.html',{
        'leader' : user_P,
        'gitname' : gitusername,
        'user': user,
        'profile' : profile,
        'p' : lang_percentage,
        'rank' : get_overall_rank(gitusername)
        
    })

def get_lang_rank(githubName):
    x = requests.get(f'https://api.github.com/users/{githubName}/repos')
    data = x.json()
    prog = []
    projects = []
    lang_dict= {}
    lang_percentage = {}
    ranking = {}
    for i in range(len(data)):
        projects.append(data[i]['name'])

    for project in projects:
        html_text = requests.get(f'https://github.com/{githubName}/{project}').content
        soup = BeautifulSoup(html_text, 'lxml')
        languages = soup.find_all('a',class_ = 'd-inline-flex flex-items-center flex-nowrap Link--secondary no-underline text-small mr-3')
        for lang in languages:
            d = lang.find_all('span')
            for a in d:
                prog.append(a.text.replace("%",""))
        lang_dict[project] = {prog[i]: prog[i + 1] for i in range(0, len(prog), 2)}
        prog[:] = []
    df = pd.DataFrame(lang_dict)
    df.index.name = "languages"
    df = df.astype(float)
    df = df.reset_index(level=0)    
    profile = Profile.objects.get(githubName = githubName)
    d = profile.userID
    for lang in list(df['languages']):
        rank = 1
        try: 
            p = list(LeaderBoards.objects.order_by("-"+lang))
            for i in p:
                ranking[i.userID] = rank
                rank +=1
            lang_percentage[lang] = ranking[d]
        except FieldError:
            pass
    return lang_percentage


def get_overall_rank(githubName):
    profile = Profile.objects.get(githubName = githubName)
    d = profile.userID
    ranking = {}
    rank = 1
    p = list(LeaderBoards.objects.order_by("-overallScore"))
    for i in p:
        ranking[i.userID] = rank
        rank +=1
    return ranking[d]