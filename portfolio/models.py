from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass


class Profile(models.Model):
    pass


class Course(models.Model):
    pass


class YearLevel(models.Model):
    pass


class LeaderBoards(models.Model):
    pass