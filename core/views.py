from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistroForm

def home(request):
    return render(request, 'core/home.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    
    return render(request, 'registration/signup.html', {'form': form})

def about(request):
    return render(request, 'core/about.html')

def probar_base(request):
    return render(request, 'core/base.html')