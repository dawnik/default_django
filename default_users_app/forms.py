from django import forms
from .models import Termin


class TerminForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Termin
        fields = ['status', 'telefon', 'kwota']
