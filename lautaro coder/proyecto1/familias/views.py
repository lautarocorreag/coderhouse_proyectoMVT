from django.shortcuts import render, redirect
from .forms import FamiliaForm
from .models import Familia

def lista_familias(request):
    familias = Familia.objects.all()
    return render(request, 'familias/lista_familias.html', {'familias': familias})

def agregar_familia(request):
    if request.method == 'POST':
        form = FamiliaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_familias')
    else:
        form = FamiliaForm()
    return render(request, 'familias/agregar_familia.html', {'form': form})

def editar_familia(request, id):
    familia = Familia.objects.get(id=id)
    if request.method == 'POST':
        form = FamiliaForm(request.POST, instance=familia)
        if form.is_valid():
            form.save()
            return redirect('lista_familias')
    else:
        form = FamiliaForm(instance=familia)
    return render(request, 'familias/editar_familia.html', {'form': form})



