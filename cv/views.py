from django.contrib.auth.models import User
from fpdf import FPDF
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from .form import ProfileForm, EducationForm, ExperienceForm, SkillForm, Interest_HobbyForm
from . models import Profile, Education, Experience, Skill, Interest_Hobby
from . import utils

class GenerateCV(View):
    def get(self, request):
        if(self.request.user.is_authenticated):
            profile = Profile.objects.filter(user=self.request.user)
            education = Education.objects.filter(user=self.request.user)
            experience = Experience.objects.filter(user=self.request.user)
            skill = Skill.objects.filter(user=self.request.user)
            ih = Interest_Hobby.objects.filter(user=self.request.user)
            context={'profile':profile, 'education':education, 'experience':experience, 'skill':skill, 'ih':ih}
            pdf = utils.render_to_pdf('cv/cv.html', context_dict=context)
            return HttpResponse(pdf, content_type='application/pdf')
        else:
            redirect('login')
    
class ReviewCV(View):
    def get(self, request):
        if(self.request.user.is_authenticated):
            profile = Profile.objects.filter(user=self.request.user)
            education = Education.objects.filter(user=self.request.user)
            experience = Experience.objects.filter(user=self.request.user)
            skill = Skill.objects.filter(user=self.request.user)
            ih = Interest_Hobby.objects.filter(user=self.request.user)

            return render(request, 'cv/cv.html', context={'profile':profile, 'education':education, 'experience':experience, 'skill':skill, 'ih':ih})

        else:
            redirect('login')

class ProfileV(View):
    def get(self, request):
        if(self.request.user.is_authenticated):
            form = ProfileForm()
            profile = Profile.objects.filter(user=self.request.user)
            return render(request,'cv/profile.html', context={"form":form, "profile":profile})
        else:
            return redirect('login')

    def post(self, request):
        if(self.request.user.is_authenticated):
            form = ProfileForm(request.POST)
            profile = Profile.objects.filter(user=self.request.user)
            if(form.is_valid()):
                data = form.cleaned_data
                name = data['name']
                address = data['address']
                phone = data['phone']
                obj = Profile.objects.filter(user=self.request.user)
                if obj:
                    obj[0].name = name
                    obj[0].address = address
                    obj[0].phone = phone
                    obj[0].save()
                else:
                    Profile.objects.create(user=self.request.user, name=name, address=address, phone=phone)
                profile = Profile.objects.filter(user=self.request.user)
                return render(request,'cv/profile.html', context={"form":form, "profile":profile})
            return render(request, 'cv/profile.html', context={"form":form, "profile":profile})
        else:
            return redirect('login')        

class EducationV(View):
    def get(self, request):
        if(self.request.user.is_authenticated):
            form = EducationForm()
            allEd = Education.objects.filter(user=self.request.user)
            return render(request, 'cv/education.html', context={"form":form, 'education':allEd})
        else:
            return redirect('login')
    
    def post(self, request):
        if(self.request.user.is_authenticated):
                form = EducationForm(request.POST)
                allEd = Education.objects.filter(user=self.request.user)
                if(form.is_valid()):
                    data = form.cleaned_data
                    user = self.request.user
                    degree = data['degree']
                    school = data['school']
                    percentage = data['percentage']
                    ed_from = data['ed_from']
                    ed_to = data['ed_to']
                    obj=Education.objects.filter(user=user, degree=degree)
                    print(obj)
                    if (obj):
                        obj[0].degree = degree
                        obj[0].school = school
                        obj[0].percentage = percentage
                        obj[0].ed_from = ed_from
                        obj[0].ed_to = ed_to
                        obj[0].save()
                    else:
                        Education.objects.create(user=user, degree=degree, school=school, percentage=percentage, ed_from=ed_from, ed_to=ed_to)
                    allEd = Education.objects.filter(user=user)
                    return render(request, 'cv/education.html', context={"form":form, 'education':allEd})
                return render(request, 'cv/education.html', context={"form":form, 'education':allEd})
        else:
            return redirect('login') 

class EducationDelete(View):
    def get(self, request, id):
        if(self.request.user.is_authenticated):
            obj = Education.objects.filter(pk=id)
            if obj:
                if(obj[0].user == self.request.user):
                    obj[0].delete()
            return redirect('education_form')
        return redirect('login')

class ExperiencV(View):
    def get(self, request):
        if(self.request.user.is_authenticated):
            form = ExperienceForm()
            experience = Experience.objects.filter(user=self.request.user)
            return render(request, 'cv/experience.html', context={"form":form, 'experience':experience})
        else:
            return redirect('login')
    
    def post(self, request):
        if(self.request.user.is_authenticated):
                form = ExperienceForm(request.POST)
                experience = Experience.objects.filter(user=self.request.user)
                if(form.is_valid()):
                    data = form.cleaned_data
                    ex_title = data['ex_title']
                    ex_description = data['ex_description']
                    ex_from = data['ex_from']
                    ex_to = data['ex_to']
                    obj = Experience.objects.filter(user=self.request.user, title=ex_title)
                    if obj:
                        obj[0].title = ex_title
                        obj[0].description = ex_description
                        obj[0].ex_from = ex_from
                        obj[0].ex_to = ex_to
                    else:
                        Experience.objects.create(user=self.request.user, title=ex_title, description=ex_description
                        ,ex_from=ex_from, ex_to=ex_to)
                    experience = Experience.objects.filter(user=self.request.user)
                    return render(request, 'cv/experience.html', context={"form":form, 'experience':experience})
                return render(request, 'cv/experience.html', context={"form":form, 'experience':experience})
        else:
            return redirect('login')

class ExperienceDelete(View):
    def get(self, request, id):
        if(self.request.user.is_authenticated):
            obj = Experience.objects.filter(pk=id)
            if obj:
                if(obj[0].user == self.request.user):
                    obj[0].delete()
            return redirect('education_form')
        return redirect('login')

class SkillV(View):
    def get(self, request):
         if(self.request.user.is_authenticated):
            form = SkillForm()
            skill = Skill.objects.filter(user=self.request.user)
            return render(request, 'cv/skill.html', context={"form":form, 'skill':skill})
         else:
            return redirect('login')
    
    def post(self, request):
        if(self.request.user.is_authenticated):
                form = SkillForm(request.POST)
                skill = Skill.objects.filter(user=self.request.user)
                if(form.is_valid()):
                    data = form.cleaned_data
                    title = data['sk_title']
                    rating = data['sk_rating']
                    obj = Skill.objects.filter(user=self.request.user, title=title)
                    if obj:
                        obj[0].title = title
                        obj[0].rating = rating
                        obj[0].save()
                    else:
                        Skill.objects.create(user=self.request.user, title=title, rating=rating)
                    skill = Skill.objects.filter(user=self.request.user)
                    return render(request, 'cv/skill.html', context={"form":form, 'skill':skill})
                return render(request, 'cv/skill.html', context={"form":form, 'skill':skill})
        else:
            return redirect('login')

class SkillDelete(View):
    def get(self, request, id):
        if(self.request.user.is_authenticated):
            obj = Skill.objects.filter(pk=id)
            if obj:
                if(obj[0].user == self.request.user):
                    obj[0].delete()
            return redirect('education_form')
        return redirect('login')

class Interest_HobbyV(View):
    def get(self, request):
         if(self.request.user.is_authenticated):
            form = Interest_HobbyForm()
            ih = Interest_Hobby.objects.filter(user=self.request.user)
            return render(request, 'cv/interest_hobby.html', context={"form":form, 'ih':ih})
         else:
            return redirect('login')
        
    def post(self, request):
        if(self.request.user.is_authenticated):
                form = Interest_HobbyForm(request.POST)
                ih = Interest_Hobby.objects.filter(user=self.request.user)
                if(form.is_valid()):
                    data = form.cleaned_data
                    title = data['ih_title']
                    iorh = data['iorh']
                    obj = Interest_Hobby.objects.filter(user=self.request.user, title=title)
                    if obj:
                        obj[0].title = title
                        obj[0].iorh = iorh
                        obj[0].save()
                    else:
                        Interest_Hobby.objects.create(user=self.request.user, title= title, iorh=iorh)
                    ih = Interest_Hobby.objects.filter(user=self.request.user)
                    return render(request, 'cv/interest_hobby.html', context={"form":form, 'ih':ih})
                return render(request, 'cv/interest_hobby.html', context={"form":form, 'ih':ih})
        else:
            return redirect('login')

class Interest_Hobby_Delete(View):
    def get(self, request, id):
        if(self.request.user.is_authenticated):
            obj = Interest_Hobby.objects.filter(pk=id)
            if obj:
                if(obj[0].user == self.request.user):
                    obj[0].delete()
            return redirect('education_form')
        return redirect('login')