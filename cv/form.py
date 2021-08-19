from django import forms
from django.core import validators
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.shortcuts import render
from  . import models
from django.forms.forms import Form


class ProfileForm(forms.Form):
    #PROFILE
    phoneRegex = RegexValidator(regex=r"\+92\d{10}$")

    name = forms.CharField(max_length=32)
    address = forms.CharField(max_length=64)
    phone = forms.CharField(max_length=13, validators=[phoneRegex])

class EducationForm(forms.Form):
    #EDUCATION
    DEGREE_TYPES = [('M', 'Matric'),
	    ('I', 'Intermediate'),
	    ('G', 'Graduation'),
	    ('P', 'Master')]
    degree = forms.ChoiceField(choices=DEGREE_TYPES)
    school = forms.CharField(max_length=32)
    percentage = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    ed_from = forms.DateField(label="From",widget=forms.DateInput(attrs={'type':'date'}))
    ed_to = forms.DateField(label="To:",widget=forms.DateInput(attrs={'type':'date'}))    

class ExperienceForm(forms.Form):
    #EXPERIENCE
    ex_title = forms.CharField(label="Job Title:",max_length=32)
    ex_description = forms.CharField(label="Job Description:",max_length=128)
    ex_from = forms.DateField(label="From:",widget=forms.DateInput(attrs={'type':'date'}))
    ex_to = forms.DateField(label="To:",widget=forms.DateInput(attrs={'type':'date'}))

class SkillForm(forms.Form):
    #SKILL
    sk_title = forms.CharField(label="Skill Title:",max_length=32)
    sk_rating = forms.IntegerField(label="Rating (0-10):",validators=[MinValueValidator(0), MaxValueValidator(10)])

class Interest_HobbyForm(forms.Form):
    #INTEREST_HOBBY
    ih_title = forms.CharField(label="Interest/Hobby:", max_length=32)
    iorh = forms.BooleanField(label="Hobby:")



