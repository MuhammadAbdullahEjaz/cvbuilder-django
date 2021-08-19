from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Profile, Education, Experience ,Skill ,Interest_Hobby
# Register your models here.

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Interest_Hobby)
