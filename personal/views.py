"""CRUD de Empleados y Cargos con Vistas Basadas en Funciones (VBF)."""
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cargo, Empleado
from .forms import CargoForm, EmpleadoForm


def home(request):
    return render(request, 'home.html')


# ---------- CRUD Cargos ----------

def cargo_list(request):
    cargos = Cargo.objects.all()
    return render(request, 'cargo_list.html', {'cargos': cargos})


def cargo_create(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo_list')
    else:
        form = CargoForm()
    return render(request, 'cargo_form.html', {'form': form, 'titulo': 'Registrar cargo'})


def cargo_update(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('cargo_list')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'cargo_form.html', {'form': form, 'titulo': 'Editar cargo'})


def cargo_delete(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        cargo.delete()
        return redirect('cargo_list')
    return render(request, 'cargo_confirm_delete.html', {'cargo': cargo})


# ---------- CRUD Empleados ----------

def empleado_list(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado_list.html', {'empleados': empleados})


def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'empleado_form.html', {'form': form, 'titulo': 'Registrar empleado'})


def empleado_update(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado_list')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleado_form.html', {'form': form, 'titulo': 'Editar empleado'})


def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('empleado_list')
    return render(request, 'empleado_confirm_delete.html', {'empleado': empleado})
