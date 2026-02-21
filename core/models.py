from django.db import models

class MensajeContacto(models.Model):
    """Guarda los datos y el mensaje que envían los usuarios desde el formulario de la web."""
    id = models.BigAutoField(primary_key= True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre del remitente")
    email = models.EmailField(verbose_name="Correo de contacto")
    asunto = models.CharField(max_length=200)
    contenido = models.TextField(verbose_name="Mensaje")
    
    fecha_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-fecha_envio'] 

    def __str__(self):
        return f"Mensaje de {self.nombre} - {self.asunto}"