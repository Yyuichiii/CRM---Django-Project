from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class register(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']




