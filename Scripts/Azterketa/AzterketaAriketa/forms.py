from django import forms
from .models import Pazientea

class PazienteForm(forms.ModelForm):
 class Meta:
    model=Pazientea
    fields=['izena','abizena','historiala']
