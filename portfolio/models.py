from turtle import ondrag
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
# Create your models here.

class User(AbstractUser):
    pass

class Course(models.Model):
    course = models.CharField(max_length=50)


class YearLevel(models.Model):
    yearLevel = models.CharField(max_length=50)



class LeaderBoards(models.Model):
    pass


class Profile(models.Model):
    userID = models.ForeignKey(User, on_delete=CASCADE, related_name= 'userProfile' )
    courseID = models.ForeignKey(Course, on_delete=CASCADE, related_name='userCourse' )
    yearId = models.ForeignKey(YearLevel, on_delete=CASCADE, related_name= 'userYearLevel')







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