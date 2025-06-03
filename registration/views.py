from django.shortcuts import render,redirect
from django.contrib import auth, messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .froms import RegistrationLoginForm,UserRegistrationForm,ProfileForm

from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from orders.models import Order,OrderItem

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
        return HttpResponseRedirect(reverse('users:saunas_list'))
  else:
    form = RegistrationLoginForm()
      
      
    return render(request,'registration/login.html',{'form':form})

  
def register(request):
  if request.method=="POST":
    form = UserRegistrationForm(data=request.POST)
    if form.is_valid():
      form.save()
      user = form.instance
      auth.loin(request,user)
      messages.success(
        request,f'{user.username}, Регистрация прошла успешно'
      )
      return HttpResponseRedirect(reverse('registration:login'))
  else:
    form = UserRegistrationForm()
  return render(request,'registration/register.html')

@login_required
def profile(request):
  if request.method=="POST":
    form = ProfileForm(data=request.POST, isinstance=request.user,
                       files=request.FILES)
    if form.is_valid():
      form.save()
      messages.success(request,"Профиль был изменен")
      return HttpResponseRedirect(reverse('registration:profile'))
  else:
    form = ProfileForm(isinstance=request.user)
  
  orders = Order.objects.filter(user=request.user).prefetch_related(
    Prefetch(
      'items',
      queryset=OrderItem.objects.select_related('sauna'),
    )
  ).order_by('-id')
  return render(request,'registration/profile.html',
                {'form':form,
                 'orders':orders})

  
def logout(request):
  auth.logout(request)
  return redirect(reverse('users:saunas_list'))