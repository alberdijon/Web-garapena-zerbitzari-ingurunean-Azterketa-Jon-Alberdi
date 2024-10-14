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