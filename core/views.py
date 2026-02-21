from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import RegistroForm
from practicas.models import RegistroPractica, Tutor


def home(request):
    contexto = {}
    
    if request.user.is_authenticated:
        mi_diario = RegistroPractica.objects.filter(alumno=request.user).first()
        
        if mi_diario:
            mi_tutor = Tutor.objects.filter(empresa=mi_diario.empresa).first()
            contexto['mi_tutor'] = mi_tutor
            
    return render(request, 'core/home.html', contexto)

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  
            return redirect('home')
    else:
        form = RegistroForm()
    
    return render(request, 'registration/signup.html', {'form': form})

def about(request):
    return render(request, 'core/about.html')