from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Registration


class RegistrationLoginForm(AuthenticationForm):
  username = forms.CharField()
  password = forms.CharField()
  
  class Meta:
    model = Registration
    fields = ['username','password']