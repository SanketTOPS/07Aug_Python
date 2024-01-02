from django import forms
from .models import *


class signupform(forms.ModelForm):
    class Meta:
        model=newuser
        fields='__all__'