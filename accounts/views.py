from django.shortcuts import redirect, render
from .forms import  MyUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
# from .models import Profile

# Create your views here.

class UserCreationView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form): 
        form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        if user:
            login(self.request, user)
            return redirect('home')
        else:
            return self.form_invalid(form)



class MyLoginView(LoginView):
    template_name = 'login.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)   
    
   

def profileID(request, id):
    return render(request,'profile.html')         