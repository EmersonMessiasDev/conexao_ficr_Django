from dataclasses import fields
import email
from re import U
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class FormHomepage(forms.Form):
    email= forms.EmailField()
    

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = Usuario
        fields  = ("username", "email", "password1", "password2")