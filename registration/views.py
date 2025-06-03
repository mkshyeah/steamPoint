from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponseRedirect
from .froms import RegistrationLoginForm

# Create your views here.
def login(request):
  if request.method=="POST":
    form = RegistrationLoginForm(data=request.POST)
    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username,
                               password=password)
      
      if user:
        auth.login(request,user)
        return HttpResponseRedirect(reverse('users:saunas'))
    else:
      form = RegistrationLoginForm()
      
      
    return render(request,'registration/login.html',{'form':form})

  
def register(request):
  return render(request,'registration/register.html')

  
def profile(request):
  return render(request,'registration/profile.html')

  
def logout(request):
  ...