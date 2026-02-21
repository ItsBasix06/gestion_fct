from django import forms
from .models import Empresa, Tutor, RegistroPractica

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'

class RegistroPracticaForm(forms.ModelForm):
    # Ponemos un selector de fecha bonito para el formulario
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = RegistroPractica
        # FÍJATE AQUÍ: Solo pedimos estos datos, omitimos 'alumno'
        fields = ['empresa', 'fecha', 'horas', 'descripcion']