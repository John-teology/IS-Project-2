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


# Create your views here


nameProb = {
    '1C Enterprise' : 'CEnterprise',
    'ASP.NET' : 'ASPNET',
    'C#':'CSharp',
    'C++':'Cplus',
    'F#':'FSharp',
    'HTML+RAZOR':'HTML_Razor',
    'Jupyter Notebook':'JupyterNotebook',
    'Objective-C':'ObjectiveC',
    'Objective-C++':'ObjectiveCplus',
    'OpenEdge ABL':'OpenEdgeABL',
    'Perl 6':'Perl6',
    'Protocol Buffer':'ProtocolBuffer',
}

languages = [ '1C Enterprise','ASP.NET','ActionScript','Apex','Assembly','Ballerina',
'Batchfile',
'Blazor',
'C',
'C#',
'C++',
'COBOL',
'CSS',
'Clojure',
'CoffeeScript',
'Crystal',
'Cucumber',
'Dart',
'Delphi',
'Dockerfile',
'EJS',
'EPP',
'ERB',
'Ebuild',
'Elixir',
'Elm',
'Erlang',
'F#',
'Fortran',
'Go',
'Groovy',
'HCL',
'HTML',
'HTML+Razor',
'Haskell',
'Haxe',
'HiveQL',
'JSON',
'Java',
'JavaScript',
'Julia',
'Jupyter Notebook',
'Kivy',
'Kotlin',
'LabVIEW',
'Less',
'Lex',
'Limbo',
'Liquid',
'Lua',
'M',
'MATLAB',
'Makefile',
'Mathematica',
'Mercury',
'Nginx',
'Nix',
'Objective-C',
'Objective-C++',
'OpenEdge ABL',
'PHP',
'PLSQL',
'PLpgSQL',
'Perl',
'Perl 6',
'PowerBuilder',
'Powershell',
'Prolog',
'Protocol Buffer',
'Puppet',
'Python',
'QML',
'R',
'Raku',
'Robot',
'Ruby',
'Rust',
'SASS',
'SCSS',
'SQL',
'SQLPL',
'Scala',
'Shell',
'Smalltalk',
'Solidity',
'Stata',
'Stylus',
'Svelte',
'Swift',
'TSQL',
'TypeScript',
'Vue',
'XML',
'Xtend',
'Xtext',
'YAML',
'Yacc',
'Zig',

]

def index(request):
    return render(request, "portfolio/index.html")


# https://avatars.githubusercontent.com/John-teology github profile image hehe
def webscrp(githubName,option=""):
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

    if option == "lang_dict":
        return lang_dict
    else:    
        return df
    



def get_score(githubName,user,course_id,yearlevel_id):
    df = webscrp(githubName)
    into_db = { }
    for d in df['languages']:
        val = df[df['languages'] == d ]['lang_score']
        into_db[d] = float(val.values)

    for keys in list(into_db.keys()):
        for key,value in nameProb.items():
            if keys == key:
                into_db[value] = into_db.pop(keys)

    into_db['userID'] = user
    into_db['courseID'] = course_id
    into_db['yearID'] = yearlevel_id
    into_db['overallScore'] = df['lang_score'].sum()

    saving_score(into_db,user)
    
    
def saving_score(input,user):
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
        saving_score(input,user)


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
        return HttpResponseRedirect(reverse('profile', args=(githubName,)))
    

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
    lang_rank = get_lang_rank(gitusername)
    rank = get_overall_rank(gitusername)
    repos = webscrp(gitusername,'lang_dict')
    return render(request, 'portfolio/profile.html',{
        'leader' : user_P,
        'gitname' : gitusername,
        'user': user,
        'profile' : profile, 
        'p' : lang_rank,
        'rank' : rank,
        'repos' : repos
        
    })

def get_lang_rank(githubName):
    df = webscrp(githubName)
    ranking = {}
    lang_percentage= {}
    profile = Profile.objects.get( githubName = githubName)
    user = profile.userID
    laad =  list(df['languages'])
    for key,value in nameProb.items(): #for naming convention
        l = list(map(lambda x: x.replace(key, value), laad))
    for lang in l:
        rank = 1
        try: 
            p = list(LeaderBoards.objects.order_by("-"+lang))
            for i in p:
                ranking[i.userID] = rank
                rank +=1
            lang_percentage[lang] = ranking[user]
        except FieldError:
            pass
    return lang_percentage


def get_overall_rank(githubName):
    profile = Profile.objects.get(githubName = githubName)
    user = profile.userID
    ranking = {}
    rank = 1
    p = list(LeaderBoards.objects.order_by("-overallScore"))
    for i in p:
        ranking[i.userID] = rank
        rank +=1
    return ranking[user]




def refresh(request,githubname):
    profile = Profile.objects.get(githubName = githubname)
    user = profile.userID
    lead = LeaderBoards.objects.get(userID = user)
    course_id = lead.courseID
    yearlevel_id = lead.yearID
    if request.method == 'POST':
        get_score(githubname,user,course_id,yearlevel_id)

    return HttpResponseRedirect(reverse('profile', args=(githubname,)))


def leaderboard(request):
    course = Course.objects.all()
    year = YearLevel.objects.all()
    by_what = '-overallScore'
    d = {}
    select1 = 'Select your course'
    select2 = 'Select your Year Level'
    select3 = 'Languages'
    if request.method == 'POST':
        lang = 'overallScore'
        if request.POST.get('courseid'):
            c_id = request.POST['courseid']
            c = Course.objects.get(pk = c_id)
            d['courseID'] = c
            select1 = c

        if request.POST.get('yearlevelid'):
            y_id = request.POST['yearlevelid']
            date = YearLevel.objects.get(pk = y_id)
            d['yearID'] = date
            select2 = date

        if request.POST.get('languages'):
            lang = request.POST['languages']
            select3 = request.POST['languages']
        try:
            data = LeaderBoards.objects.filter(**d).order_by('-' +lang)
        except FieldError:
            lang = nameProb[lang]
            data = LeaderBoards.objects.filter(**d).order_by('-' +lang)

    else:
        lang = ''
        data= LeaderBoards.objects.order_by(by_what)
        
    return render(request,'portfolio/leaderboards.html',{
        'courses': course,
        'yearlevels':year,
        'languages': languages,
        'data' : data,
        'select1': select1,
        'select2': select2,
        'select3': select3,
        'lang' : lang,
    })

def redirect(request,userid):
    p = Profile.objects.get(userID = userid)

    return HttpResponseRedirect(reverse('profile',args=(p.githubName,)))



