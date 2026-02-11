from django.contrib import admin
from .models import MensajeContacto

class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "email", "asunto", "fecha_envio")
    
    search_fields = ("nombre", "email", "asunto")
    
    list_filter = ("fecha_envio",)
    
    readonly_fields = ("fecha_envio",)

admin.site.register(MensajeContacto, MensajeContactoAdmin)