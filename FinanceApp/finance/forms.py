from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import TransactionModel,Goal


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields=["username","email","password1","password2"]


class TranscationForm(forms.ModelForm):
    class Meta:
        model = TransactionModel
        fields = ['title','amount','Transcation_type','date','category']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
class GoalForm(forms.ModelForm):
    class Meta:
        goal = Goal
        fields = ['name','amount','deadline']
        widgets ={
            'deadline':forms.DateInput(attrs={'type':'date'})
        }        