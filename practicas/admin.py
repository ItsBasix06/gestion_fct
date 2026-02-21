from django.contrib import admin
from .models import Empresa, Tutor, RegistroPractica

# Personalización del panel para ver las empresas en columnas
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre',)

# Para ver qué tutor pertenece a cada empresa
class TutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'cargo')
    list_filter = ('empresa',)

# Para que el profesor vea el diario ordenado por alumno y fecha
class RegistroPracticaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'alumno', 'empresa', 'horas')
    list_filter = ('alumno', 'empresa', 'fecha')

# Registro de los modelos con sus clases de administración
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(RegistroPractica, RegistroPracticaAdmin)