from django import forms
from .models import *


class signupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields=['password']