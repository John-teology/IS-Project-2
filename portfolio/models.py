from turtle import ondrag
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
# Create your models here.

class User(AbstractUser):
    pass

class Course(models.Model):
    course = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.course}"

class YearLevel(models.Model):
    yearLevel = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.yearLevel}"


class Profile(models.Model):
    userID = models.ForeignKey(User, on_delete=CASCADE, related_name= 'userProfile' )
    courseID = models.ForeignKey(Course, on_delete=CASCADE, related_name='profile_Course', null=True )
    yearID = models.ForeignKey(YearLevel, on_delete=CASCADE, related_name= 'profile_userYearLevel' , null=True)
    nickname = models.CharField(max_length=100, blank=True)
    githubName = models.CharField(max_length=100)
    aboutMe = models.TextField(max_length=300)


class LeaderBoards(models.Model):
    userID = models.ForeignKey(User, on_delete=CASCADE, related_name= 'userLeaderboard' )
    courseID = models.ForeignKey(Course, on_delete=CASCADE ,related_name='userCourse' , null=True)
    yearID = models.ForeignKey(YearLevel, on_delete=CASCADE,  related_name= 'userYearLevel',null=True )
    overallScore = models.FloatField(default=0,blank=True)
    CEnterprise = models.FloatField(default=0,blank=True, verbose_name='1C Enterprise') 
    ASPNET = models.FloatField(default=0,blank=True, verbose_name='ASP.NET') 
    ActionScript = models.FloatField(default=0,blank=True)
    Apex = models.FloatField(default=0,blank=True)
    Assembly = models.FloatField(default=0,blank=True)
    Ballerina = models.FloatField(default=0,blank=True)
    Batchfile = models.FloatField(default=0,blank=True)
    Blazor = models.FloatField(default=0,blank=True)
    C = models.FloatField(default=0,blank=True)
    CSharp = models.FloatField(default=0,blank=True, verbose_name='C#')
    Cplus = models.FloatField(default=0,blank=True,verbose_name='C++')
    COBOL = models.FloatField(default=0,blank=True)
    CSS = models.FloatField(default=0,blank=True)
    Clojure = models.FloatField(default=0,blank=True)
    CoffeeScript = models.FloatField(default=0,blank=True)
    Crystal = models.FloatField(default=0,blank=True)
    Cucumber = models.FloatField(default=0,blank=True)
    Dart = models.FloatField(default=0,blank=True)
    Delphi = models.FloatField(default=0,blank=True)
    Dockerfile = models.FloatField(default=0,blank=True)
    EJS = models.FloatField(default=0,blank=True)
    EPP = models.FloatField(default=0,blank=True)
    ERB = models.FloatField(default=0,blank=True)
    Ebuild = models.FloatField(default=0,blank=True)
    Elixir = models.FloatField(default=0,blank=True)
    Elm = models.FloatField(default=0,blank=True)
    Erlang = models.FloatField(default=0,blank=True)
    FSharp = models.FloatField(default=0,blank=True,verbose_name='F#')
    Fortran = models.FloatField(default=0,blank=True)
    Go = models.FloatField(default=0,blank=True)
    Groovy = models.FloatField(default=0,blank=True)
    HCL = models.FloatField(default=0,blank=True)
    HTML = models.FloatField(default=0,blank=True)
    HTML_Razor = models.FloatField(default=0,blank=True,verbose_name='HTML+RAZOR')
    Haskell = models.FloatField(default=0,blank=True)
    Haxe = models.FloatField(default=0,blank=True)
    HiveQL = models.FloatField(default=0,blank=True)
    JSON = models.FloatField(default=0,blank=True)
    Java = models.FloatField(default=0,blank=True)
    JavaScript = models.FloatField(default=0,blank=True)
    Julia = models.FloatField(default=0,blank=True)
    JupyterNotebook = models.FloatField(default=0,blank=True, verbose_name='Jupyter Notebook')
    Kivy = models.FloatField(default=0,blank=True)
    Kotlin = models.FloatField(default=0,blank=True)
    LabVIEW = models.FloatField(default=0,blank=True)
    Less = models.FloatField(default=0,blank=True)
    Lex = models.FloatField(default=0,blank=True)
    Limbo = models.FloatField(default=0,blank=True)
    Liquid = models.FloatField(default=0,blank=True)
    Lua = models.FloatField(default=0,blank=True)
    M = models.FloatField(default=0,blank=True)
    MATLAB = models.FloatField(default=0,blank=True)
    Makefile = models.FloatField(default=0,blank=True)
    Mathematica = models.FloatField(default=0,blank=True)
    Mercury = models.FloatField(default=0,blank=True)
    Nginx = models.FloatField(default=0,blank=True)
    Nix = models.FloatField(default=0,blank=True)
    ObjectiveC = models.FloatField(default=0,blank=True, verbose_name='Objective-C')
    ObjectiveCplus = models.FloatField(default=0,blank=True, verbose_name='Objective-C++')
    OpenEdgeABL = models.FloatField(default=0,blank=True, verbose_name='OpenEdge ABL')
    PHP = models.FloatField(default=0,blank=True)
    PLSQL = models.FloatField(default=0,blank=True)
    PLpgSQL = models.FloatField(default=0,blank=True)
    Perl = models.FloatField(default=0,blank=True)
    Perl6 = models.FloatField(default=0,blank=True, verbose_name='Perl 6')
    PowerBuilder = models.FloatField(default=0,blank=True)
    Powershell = models.FloatField(default=0,blank=True)
    Prolog = models.FloatField(default=0,blank=True)
    ProtocolBuffer = models.FloatField(default=0,blank=True, verbose_name= 'Protocol Buffer')
    Puppet = models.FloatField(default=0,blank=True)
    Python = models.FloatField(default=0,blank=True)
    QML = models.FloatField(default=0,blank=True)
    R = models.FloatField(default=0,blank=True)
    Raku = models.FloatField(default=0,blank=True)
    Robot = models.FloatField(default=0,blank=True)
    Ruby = models.FloatField(default=0,blank=True)
    Rust = models.FloatField(default=0,blank=True)
    SASS = models.FloatField(default=0,blank=True)
    SCSS = models.FloatField(default=0,blank=True)
    SQL = models.FloatField(default=0,blank=True)
    SQLPL = models.FloatField(default=0,blank=True)
    Scala = models.FloatField(default=0,blank=True)
    Shell = models.FloatField(default=0,blank=True)
    Smalltalk = models.FloatField(default=0,blank=True)
    Solidity = models.FloatField(default=0,blank=True)
    Stata = models.FloatField(default=0,blank=True)
    Stylus = models.FloatField(default=0,blank=True)
    Svelte = models.FloatField(default=0,blank=True)
    Swift = models.FloatField(default=0,blank=True)
    TSQL = models.FloatField(default=0,blank=True)
    TypeScript = models.FloatField(default=0,blank=True)
    Vue = models.FloatField(default=0,blank=True)
    XML = models.FloatField(default=0,blank=True)
    Xtend = models.FloatField(default=0,blank=True)
    Xtext = models.FloatField(default=0,blank=True)
    YAML = models.FloatField(default=0,blank=True)
    Yacc = models.FloatField(default=0,blank=True)
    Zig = models.FloatField(default=0,blank=True)








"""
[

1C Enterprise
ASP.NET
ActionScript
Apex
Assembly
Ballerina
Batchfile
Blazor
C
C#
C++
COBOL
CSS
Clojure
CoffeeScript
Crystal
Cucumber
Dart
Delphi
Dockerfile
EJS
EPP
ERB
Ebuild
Elixir
Elm
Erlang
F#
Fortran
Go
Groovy
HCL
HTML
HTML+Razor
Haskell
Haxe
HiveQL
JSON
Java
JavaScript
Julia
Jupyter Notebook
Kivy
Kotlin
LabVIEW
Less
Lex
Limbo
Liquid
Lua
M
MATLAB
Makefile
Mathematica
Matlab
Mercury
Nginx
Nix
Objective-C
Objective-C++
OpenEdge ABL
PHP
PLSQL
PLpgSQL
Perl
Perl 6
PowerBuilder
Powershell
Prolog
Protocol Buffer
Puppet
Python
QML
R
Raku
Robot
Ruby
Rust
SASS
SCSS
SQL
SQLPL
Scala
Shell
Smalltalk
Solidity
Stata
Stylus
Svelte
Swift
TSQL
TypeScript
Vue
XML
Xtend
Xtext
YAML
Yacc
Zig

]
"""
