from turtle import ondrag
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
# Create your models here.

class User(AbstractUser):
    pass

class Course(models.Model):
    course = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.course}"

class YearLevel(models.Model):
    yearLevel = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.yearLevel}"



class Profile(models.Model):
    userID = models.ForeignKey(User, on_delete=CASCADE, related_name= 'userProfile' )
    courseID = models.ManyToManyField(Course,  related_name='profile_Course' )
    yearId = models.ManyToManyField(YearLevel, related_name= 'profile_userYearLevel')
    githubName = models.CharField(max_length=100)
    aboutMe = models.TextField(max_length=300)


class LeaderBoards(models.Model):
    userID = models.ForeignKey(User, on_delete=CASCADE, related_name= 'userLeaderboard' )
    courseID = models.ManyToManyField(Course,  related_name='userCourse' )
    yearId = models.ManyToManyField(YearLevel, related_name= 'userYearLevel')
    overallScore = models.FloatField(default=0,blank=True)
    field0 = models.FloatField(blank=True, default=0, name='1C Enterprise')
    field1 = models.FloatField(blank=True, default=0, name='ASP.NET')     
    field2 = models.FloatField(blank=True, default=0, name='ActionScript')
    field3 = models.FloatField(blank=True, default=0, name='Apex')        
    field4 = models.FloatField(blank=True, default=0, name='Assembly')    
    field5 = models.FloatField(blank=True, default=0, name='Ballerina')   
    field6 = models.FloatField(blank=True, default=0, name='Batchfile')
    field7 = models.FloatField(blank=True, default=0, name='Blazor')
    field8 = models.FloatField(blank=True, default=0, name='C')
    field9 = models.FloatField(blank=True, default=0, name='C#')
    field10 = models.FloatField(blank=True, default=0, name='C++')
    field11 = models.FloatField(blank=True, default=0, name='COBOL')
    field12 = models.FloatField(blank=True, default=0, name='CSS')
    field13 = models.FloatField(blank=True, default=0, name='Clojure')
    field14 = models.FloatField(blank=True, default=0, name='CoffeeScript')
    field15 = models.FloatField(blank=True, default=0, name='Crystal')
    field16 = models.FloatField(blank=True, default=0, name='Cucumber')
    field17 = models.FloatField(blank=True, default=0, name='Dart')
    field18 = models.FloatField(blank=True, default=0, name='Delphi')
    field19 = models.FloatField(blank=True, default=0, name='Dockerfile')
    field20 = models.FloatField(blank=True, default=0, name='EJS')
    field21 = models.FloatField(blank=True, default=0, name='EPP')
    field22 = models.FloatField(blank=True, default=0, name='ERB')
    field23 = models.FloatField(blank=True, default=0, name='Ebuild')
    field24 = models.FloatField(blank=True, default=0, name='Elixir')
    field25 = models.FloatField(blank=True, default=0, name='Elm')
    field26 = models.FloatField(blank=True, default=0, name='Erlang')
    field27 = models.FloatField(blank=True, default=0, name='F#')
    field28 = models.FloatField(blank=True, default=0, name='Fortran')
    field29 = models.FloatField(blank=True, default=0, name='Go')
    field30 = models.FloatField(blank=True, default=0, name='Groovy')
    field31 = models.FloatField(blank=True, default=0, name='HCL')
    field32 = models.FloatField(blank=True, default=0, name='HTML')
    field33 = models.FloatField(blank=True, default=0, name='HTML+Razor')
    field34 = models.FloatField(blank=True, default=0, name='Haskell')
    field35 = models.FloatField(blank=True, default=0, name='Haxe')
    field36 = models.FloatField(blank=True, default=0, name='HiveQL')
    field37 = models.FloatField(blank=True, default=0, name='JSON')
    field38 = models.FloatField(blank=True, default=0, name='Java')
    field39 = models.FloatField(blank=True, default=0, name='JavaScript')
    field40 = models.FloatField(blank=True, default=0, name='Julia')
    field41 = models.FloatField(blank=True, default=0, name='Jupyter Notebook')
    field42 = models.FloatField(blank=True, default=0, name='Kivy')
    field43 = models.FloatField(blank=True, default=0, name='Kotlin')
    field44 = models.FloatField(blank=True, default=0, name='LabVIEW')
    field45 = models.FloatField(blank=True, default=0, name='Less')
    field46 = models.FloatField(blank=True, default=0, name='Lex')
    field47 = models.FloatField(blank=True, default=0, name='Limbo')
    field48 = models.FloatField(blank=True, default=0, name='Liquid')
    field49 = models.FloatField(blank=True, default=0, name='Lua')
    field50 = models.FloatField(blank=True, default=0, name='M')
    field51 = models.FloatField(blank=True, default=0, name='MATLAB')
    field52 = models.FloatField(blank=True, default=0, name='Makefile')
    field53 = models.FloatField(blank=True, default=0, name='Mathematica')
    field55 = models.FloatField(blank=True, default=0, name='Mercury')
    field56 = models.FloatField(blank=True, default=0, name='Nginx')
    field57 = models.FloatField(blank=True, default=0, name='Nix')
    field58 = models.FloatField(blank=True, default=0, name='Objective-C')
    field59 = models.FloatField(blank=True, default=0, name='Objective-C++')
    field60 = models.FloatField(blank=True, default=0, name='OpenEdge ABL')
    field61 = models.FloatField(blank=True, default=0, name='PHP')
    field62 = models.FloatField(blank=True, default=0, name='PLSQL')
    field63 = models.FloatField(blank=True, default=0, name='PLpgSQL')
    field64 = models.FloatField(blank=True, default=0, name='Perl')
    field65 = models.FloatField(blank=True, default=0, name='Perl 6')
    field66 = models.FloatField(blank=True, default=0, name='PowerBuilder')
    field67 = models.FloatField(blank=True, default=0, name='Powershell')
    field68 = models.FloatField(blank=True, default=0, name='Prolog')
    field69 = models.FloatField(blank=True, default=0, name='Protocol Buffer')
    field70 = models.FloatField(blank=True, default=0, name='Puppet')
    field71 = models.FloatField(blank=True, default=0, name='Python')
    field72 = models.FloatField(blank=True, default=0, name='QML')
    field73 = models.FloatField(blank=True, default=0, name='R')
    field74 = models.FloatField(blank=True, default=0, name='Raku')
    field75 = models.FloatField(blank=True, default=0, name='Robot')
    field76 = models.FloatField(blank=True, default=0, name='Ruby')
    field77 = models.FloatField(blank=True, default=0, name='Rust')
    field78 = models.FloatField(blank=True, default=0, name='SASS')
    field79 = models.FloatField(blank=True, default=0, name='SCSS')
    field80 = models.FloatField(blank=True, default=0, name='SQL')
    field81 = models.FloatField(blank=True, default=0, name='SQLPL')
    field82 = models.FloatField(blank=True, default=0, name='Scala')
    field83 = models.FloatField(blank=True, default=0, name='Shell')
    field84 = models.FloatField(blank=True, default=0, name='Smalltalk')
    field85 = models.FloatField(blank=True, default=0, name='Solidity')
    field86 = models.FloatField(blank=True, default=0, name='Stata')
    field87 = models.FloatField(blank=True, default=0, name='Stylus')
    field88 = models.FloatField(blank=True, default=0, name='Svelte')
    field89 = models.FloatField(blank=True, default=0, name='Swift')
    field90 = models.FloatField(blank=True, default=0, name='TSQL')
    field91 = models.FloatField(blank=True, default=0, name='TypeScript')
    field92 = models.FloatField(blank=True, default=0, name='Vue')
    field93 = models.FloatField(blank=True, default=0, name='XML')
    field94 = models.FloatField(blank=True, default=0, name='Xtend')
    field95 = models.FloatField(blank=True, default=0, name='Xtext')
    field96 = models.FloatField(blank=True, default=0, name='YAML')
    field97 = models.FloatField(blank=True, default=0, name='Yacc')
    field98 = models.FloatField(blank=True, default=0, name='Zig')








"""
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

"""
