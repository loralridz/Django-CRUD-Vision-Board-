from django import forms
from .models import *


class personalforms(forms.ModelForm):

    class Meta:
        model = Personal
        fields = '__all__'

class professionalforms(forms.ModelForm):
    class Meta:
        model=Professional
        fields='__all__'
