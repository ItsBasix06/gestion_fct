from django.contrib import admin
from .models import Empresa, Profesor, Alumno, EntradaDiario

admin.site.register(Empresa)
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(EntradaDiario)