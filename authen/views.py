from django.shortcuts import redirect, render, HttpResponse
from . form import UserRegistrationForm
from django.views.generic import View
# Create your views here.

class SignupV(View):
    def get(self, request):
        if(self.request.user.is_authenticated):
            form = UserRegistrationForm()
            return render(request, 'authen/signup.html', context={'form':form})
        return redirect('login')
    
    def post(self, request):
         if(self.request.user.is_authenticated):
             form = UserRegistrationForm(self.request.POST)
             if form.is_valid():
                form.save()
                return redirect('login')
             return render(request, 'authen/signup.html', context={'form':form})
         return redirect('login')