from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *


# Create your views here.
def paziente_list(request):
    pazienteZerrenda = Pazientea.objects.all()
    return render(request, 'kudeaketa/pazienteak/paziente_list.html', {"pazienteak": pazienteZerrenda})

def paziente_new(request):
    if request.method == 'POST':
        form = PazienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(paziente_list)
    else:
        form = PazienteForm()
    return render(request, 'kudeaketa/pazienteak/paziente_new.html', {'form': form})


def paziente_edit(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        izena = request.POST.get("izena", "")
        abizena = request.POST.get("abizena", "")
        historiala = request.POST.get("historiala", "")
        paziente = Pazientea.objects.get(id=id)
        paziente.izena = izena
        paziente.abizena = abizena
        paziente.historiala = historiala
        paziente.save()

        return redirect('paziente-default')
    
    else:
        pazienteZerrenda = Pazientea.objects.all()
        return render(request, 'kudeaketa/pazienteak/paziente_edit.html', {'pazienteak':pazienteZerrenda})
    

def paziente_edit_form(request, paziente_id):
    paziente = get_object_or_404(Pazientea, id = paziente_id)

    if request.method == 'POST':
        form = EditPazienteaForm(request.POST, instance=paziente)
        if form.is_valid():
            form.save()
            return redirect ('paziente-default')
    else:
        form = EditPazienteaForm(instance=paziente)
    
    return render (request, 'kudeaketa/pazienteak/paziente_new.html', {'form': form})


def paziente_delete(request):
    if request.method == 'POST':
        uid = request.POST.get("uid", "")
        Pazientea.objects.filter(id = uid).delete()
        return redirect('paziente-default')
    else:
        pazienteZerrenda = Pazientea.objects.all()
        return render(request, 'kudeaketa/pazienteak/paziente_delete.html', {'pazienteak': pazienteZerrenda})
    

def medikua_list(request):
    medikuaZerrenda = Medikua.objects.all()
    return render(request, 'kudeaketa/medikuak/medikua_list.html', {"medikuak": medikuaZerrenda})

def medikua_new(request):
    if request.method == 'POST':
        form = MedikuaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(medikua_list)
    else:
        form = MedikuaForm()
    return render(request, 'kudeaketa/medikuak/medikua_new.html', {'form': form})


def medikua_edit(request):
    if request.method == 'POST':
        id = request.POST.get("id", "")
        izena = request.POST.get("izena", "")
        abizena = request.POST.get("abizena", "")
        lanpostua = request.POST.get("lanpostua", "")
        medikua = Medikua.objects.get(id=id)
        medikua.izena = izena
        medikua.abizena = abizena
        medikua.lanpostua = lanpostua
        medikua.save()

        return redirect('medikua-default')
    
    else:
        medikuaZerrenda = Medikua.objects.all()
        return render(request, 'kudeaketa/medikuak/medikua_edit.html', {'medikuak':medikuaZerrenda})
    

def medikua_edit_form(request, medikua_id):
    medikua = get_object_or_404(Medikua, id = medikua_id)

    if request.method == 'POST':
        form = EditMedikuaForm(request.POST, instance=medikua)
        if form.is_valid():
            form.save()
            return redirect ('medikua-default')
    else:
        form = EditMedikuaForm(instance=medikua)
    
    return render (request, 'kudeaketa/medikuak/medikua_new.html', {'form': form})


def medikua_delete(request):
    if request.method == 'POST':
        uid = request.POST.get("uid", "")
        Medikua.objects.filter(id = uid).delete()
        return redirect('medikua-default')
    else:
        medikuaZerrenda = Medikua.objects.all()
        return render(request, 'kudeaketa/medikuak/medikua_delete.html', {'medikuak': medikuaZerrenda})
    

def zita_list(request):
    zitaZerrenda = Zita.objects.all()
    return render(request, 'kudeaketa/zitak/zitak_list.html', {'zitak': zitaZerrenda})

def zita_new(request):
    if request.method == 'POST':
        form=ZitaForm(request.POST)
        if form.is_valid:
            zita = form.save()
            zita.save()
        return redirect(zita_list)
    else:
        form=ZitaForm()
        return render(request, 'kudeaketa/zitak/zitak_new.html', {'form': form})