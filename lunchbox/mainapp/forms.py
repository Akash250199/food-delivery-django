from django import forms
from  mainapp.models import booking

class reservation(forms.ModelForm):
    class Meta:
        model=booking
        fields="__all__"