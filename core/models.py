from django.db import models

# Create your models here.
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del remitente")
    email = models.EmailField(verbose_name="Correo de contacto")
    asunto = models.CharField(max_length=200)
    contenido = models.TextField(verbose_name="Mensaje")
    
    # Fecha automática para saber cuándo lo enviaron
    fecha_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-fecha_envio'] # Los más nuevos primero

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.asunto}"
    


