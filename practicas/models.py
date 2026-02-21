from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    """Guarda los datos de contacto de las empresas donde se hacen las FCT."""
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre

class Tutor(models.Model):
    """Representa al responsable que supervisa al alumno dentro de la empresa."""
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    cargo = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tutor de Empresa"
        verbose_name_plural = "Tutores de Empresa"

    def __str__(self):
        return self.nombre

class RegistroPractica(models.Model):
    """Almacena la actividad diaria, las horas realizadas y el alumno que las hizo."""
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha = models.DateField()
    horas = models.DecimalField(max_digits=4, decimal_places=2)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Entrada del Diario"
        verbose_name_plural = "Entradas del Diario"

    def __str__(self):
        return f"{self.fecha} - {self.alumno.username}"