from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    convenio_firmado = models.BooleanField(default=True, verbose_name="¿Convenio activo?")
    
    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del tutor")
    email = models.EmailField(verbose_name="Correo electrónico", blank=True)
    cargo = models.CharField(max_length=100, verbose_name="Cargo en la empresa", blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="tutores")
    
    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del alumno")
    email = models.EmailField(verbose_name="Correo electrónico", blank=True)
    telefono = models.CharField(max_length=20, verbose_name="Número de teléfono", blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="alumnos")
    
    tutor_asignado = models.ForeignKey(Profesor, on_delete=models.PROTECT, verbose_name="Tutor Laboral", related_name="alumnos_a_cargo")
    
    def __str__(self):
        return self.nombre
    
class EntradaDiario(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha de la práctica")
    horas = models.DecimalField(max_digits=4, decimal_places=2, help_text="Ejemplo: 6.5")
    tareas = models.TextField(verbose_name="Tareas realizadas")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones / Aprendizaje")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']
        verbose_name = "Entrada del Diario"
        verbose_name_plural = "Entradas del Diario"

    def __str__(self):
        return f"Práctica del {self.fecha} - {self.alumno.nombre}"