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
