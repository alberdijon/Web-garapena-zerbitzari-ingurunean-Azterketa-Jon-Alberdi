from django import forms
from .models import*

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

class MedikuaForm(forms.ModelForm):
 class Meta:
    model=Medikua
    fields=['izena','abizena','lanpostua']


class EditMedikuaForm(forms.ModelForm):
  class Meta :
    model=Medikua
    fields=['izena','abizena','lanpostua']

    def __init__ (self, *args, **kwargs):
        super(EditMedikuaForm, self).__init__(*args, **kwargs)


class ZitaForm(forms.ModelForm):
  class Meta:
    model=Zita
    fields=['data', 'paziente_kodea', 'mediku_kodea']