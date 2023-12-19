from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=signupmaster
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=signupmaster
        fields=['firstname','lastname','username','password','city','state','mobile']