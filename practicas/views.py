from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Empresa, Tutor, RegistroPractica
from .forms import EmpresaForm, TutorForm, RegistroPracticaForm

@login_required
def empresa_list(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/list.html', {'empresas': empresas})

@login_required
def empresa_create(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa creada correctamente.')
            return redirect('empresa_list')
    else:
        form = EmpresaForm()
    return render(request, 'empresas/form.html', {'form': form, 'titulo': 'Nueva Empresa'})

@login_required
def empresa_update(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa actualizada.')
            return redirect('empresa_list')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'empresas/form.html', {'form': form, 'titulo': 'Editar Empresa'})

@login_required
def empresa_delete(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        empresa.delete()
        messages.success(request, 'Empresa eliminada.')
        return redirect('empresa_list')
    return render(request, 'empresas/confirm_delete.html', {'objeto': empresa})

@login_required
def tutor_list(request):
    tutores = Tutor.objects.all()
    return render(request, 'tutores/list.html', {'tutores': tutores})

@login_required
def tutor_delete(request, pk):
    tutor = get_object_or_404(Tutor, pk=pk)
    if request.method == 'POST':
        tutor.delete()
        messages.success(request, 'Tutor eliminado correctamente.')
        return redirect('tutor_list')
    return render(request, 'tutores/confirm_delete.html', {'objeto': tutor})

@login_required
def crear_tutor(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tutor añadido correctamente.')
            return redirect('home')
    else:
        form = TutorForm()
    return render(request, 'practicas/tutor.html', {'form': form})

from django.db.models import Sum # Pon esto junto a los demás imports

@login_required
def diario_list(request):
    entradas = RegistroPractica.objects.filter(alumno=request.user)
    
    total = entradas.aggregate(Sum('horas'))['horas__sum'] or 0
    
    return render(request, 'diario/list.html', {
        'entradas': entradas,
        'total_horas': total # Lo mandamos al HTML
    })

@login_required
def diario_create(request):
    if request.method == 'POST':
        form = RegistroPracticaForm(request.POST)
        if form.is_valid():
            # 1. Pausamos el guardado
            entrada = form.save(commit=False)
            # 2. Le inyectamos el usuario que está logueado ahora mismo
            entrada.alumno = request.user
            # 3. Ahora sí, guardamos definitivamente
            entrada.save()
            
            messages.success(request, 'Entrada registrada correctamente.')
            return redirect('diario_list')
    else:
        form = RegistroPracticaForm()
    return render(request, 'diario/form.html', {'form': form, 'titulo': 'Nueva Entrada'})

@login_required
def diario_update(request, pk):
    entrada = get_object_or_404(RegistroPractica, pk=pk)
    if request.method == 'POST':
        form = RegistroPracticaForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrada actualizada.')
            return redirect('diario_list')
    else:
        form = RegistroPracticaForm(instance=entrada)
    return render(request, 'diario/form.html', {'form': form, 'titulo': 'Editar Entrada'})

@login_required
def diario_delete(request, pk):
    entrada = get_object_or_404(RegistroPractica, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        messages.success(request, 'Entrada eliminada.')
        return redirect('diario_list')
    return render(request, 'diario/confirm_delete.html', {'objeto': entrada})