from django import forms
from  mainapp.models import booking

class reserv(forms.ModelForm):
    class Meta:
        model=booking
        fields="__all__"