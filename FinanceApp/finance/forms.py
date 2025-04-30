from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Transcation


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields=["username","email","password1","password2"]