from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=signupdata
        fields='__all__'