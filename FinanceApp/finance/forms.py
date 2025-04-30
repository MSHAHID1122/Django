from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Transcation


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields=["username","email","password1","password2"]


class TranscationForm(forms.ModelForm):
    class Meta:
        model = Transcation
        fields = ['title','amount','Transcation_type','date','category']