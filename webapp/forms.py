from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class register_form(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']


class login_form(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','address','city','country']

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields=['first_name','last_name','email','phone','address','city','country']



