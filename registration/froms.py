from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm,UserCreationForm

from .models import Registration


class RegistrationLoginForm(AuthenticationForm):
  username = forms.CharField()
  password = forms.CharField()
  
  class Meta:
    model = Registration
    fields = ['username','password']
    
    
    
class UserRegistrationForm(UserCreationForm):
  class Meta:
    model = Registration
    fields = {
      "first_name",
      "last_name",
      'username',
      'email',
      'password1',
      'password2',
    }
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    

class ProfileForm(UserChangeForm):
  class Meta:
    model = Registration
    fields = {
      'image',
      "first_name",
      "last_name",
      'username',
      'email',
    }
    
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    