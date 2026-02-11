from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def home(request):
    return render(request,'core/home.html')
def probar_base(request):
    return render(request,'core/base.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "¡Registro completado! Bienvenido.")
            return redirect('home')
        else:
            messages.error(request, "Error en el registro. Revisa los datos.")
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/signup.html', {'form': form})

def registro(request):
    return render(request, 'registration/signup.html', {'form': form})