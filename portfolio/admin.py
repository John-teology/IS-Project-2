from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(LeaderBoards)
admin.site.register(YearLevel)
admin.site.register(Course)

