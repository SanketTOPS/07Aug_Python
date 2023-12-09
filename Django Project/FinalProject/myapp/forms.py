from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=signupmaster
        fields='__all__'