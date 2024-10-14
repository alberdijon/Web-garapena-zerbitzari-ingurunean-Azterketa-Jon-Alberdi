from django import forms
from .models import Pazientea

class PazienteForm(forms.ModelForm):
 class Meta:
    model=Pazientea
    fields=['izena','abizena','historiala']


class EditPazienteaForm(forms.ModelForm):
  class Meta :
    model=Pazientea
    fields=['izena','abizena','historiala']

    def __init__ (self, *args, **kwargs):
        super(EditPazienteaForm, self).__init__(*args, **kwargs)
