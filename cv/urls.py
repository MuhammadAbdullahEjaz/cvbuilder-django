from django.urls import path
from . import views

urlpatterns = [
    path('',  views.ProfileV.as_view(), name='profile_form'),
    path('education/', views.EducationV.as_view(), name='education_form'),
    path('education/delete/<int:id>', views.EducationDelete.as_view(), name='education_delete'),
    path('experience/', views.ExperiencV.as_view(), name='experience_form'),
    path('experience/delete/<int:id>', views.ExperienceDelete.as_view(), name='experience_delete'),
    path('skill/', views.SkillV.as_view(), name='skill_form'),
    path('skill/delete/<int:id>', views.SkillDelete.as_view(), name='skill_delete'),
    path('interest-hobby/', views.Interest_HobbyV.as_view(), name='interest_hobby_form'),
    path('interest-hobby/delete/<int:id>', views.Interest_Hobby_Delete.as_view(), name='interest_hobby_delete'),

    path('rcv/',views.ReviewCV.as_view(), name='rcv'),
    path('gcv/',views.GenerateCV.as_view(), name='gcv'),
] 