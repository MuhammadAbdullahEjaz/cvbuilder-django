from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupV.as_view(), name='signup'),
]