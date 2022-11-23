from django import forms
from .models import AiAnswer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class FormDream(forms.Form):
    prompt = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    class Meta:
        model=AiAnswer
        fields=['prompt']


# Heredamos y extendemos
# la forma default para incluir el correo.

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']


