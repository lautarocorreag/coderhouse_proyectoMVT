from django.shortcuts import render, redirect
from .forms import FamiliaForm
from .models import Familia
from .forms import MiembroForm
from .models import Miembro

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

def agregar_miembro(request, id):
    familia = Familia.objects.get(id=id)
    if request.method == 'POST':
        form = MiembroForm(request.POST)
        if form.is_valid():
            miembro = form.save(commit=False)
            miembro.familia = familia
            miembro.save()
            return redirect('ver_familia', id)
    else:
        form = MiembroForm()
    return render(request, 'familias/agregar_miembro.html', {'form': form, 'familia': familia})

def editar_miembro(request, id):
    miembro = Miembro.objects.get(id=id)
    if request.method == 'POST':
        form = MiembroForm(request.POST, instance=miembro)
        if form.is_valid():
            form.save()
            return redirect('ver_familia', miembro.familia.id)
    else:
        form = MiembroForm(instance=miembro)
    return render(request, 'familias/editar_miembro.html', {'form': form, 'miembro': miembro})

def ver_familia(request, id):
    familia = Familia.objects.get(id=id)
    miembros = familia.miembro_set.all()
    return render(request, 'familias/ver_familia.html', {'familia': familia, 'miembros': miembros})




