# 📂 Gestion FCT: Gestión Integral de Prácticas
## 👥 Proyecto Realizado por Basi Córdoba Arcas y Javier Gómez-Comino.

Bienvenido a **Gestion FCT**, una aplicación web desarrollada en **Django** diseñada para simplificar la experiencia de las prácticas profesionales. Este proyecto nace con el objetivo de modernizar el tradicional "cuaderno de prácticas" en papel tipico que solemos llevar cada cierto tiempo, ofreciendo una plataforma centralizada donde alumnos, tutores y empresas convergen y asi evitamos el transporte de una ciudad a otro,haciendolo todo digital.




core/
│
├── static/                <-- Requisito: Ficheros estáticos [cite: 106-108]
│   └── core/
│       ├── css/
│       │   └── estilos.css  <-- Tu CSS propio
│       └── img/
│           └── logo.png     <-- Una de las 3 imágenes
│
├── templates/
│   ├── base.html          <-- El diseño principal (Bootstrap)
│   ├── core/
│   │   ├── home.html      <-- Portada
│   │   └── contacto.html  <-- Formulario forms.Form
│   └── registration/      <-- Carpetas estándar de Django
│       ├── login.html     <-- Formulario de login
│       └── signup.html    <-- Formulario de registro
│
├── forms.py               <-- Aquí va el ContactoForm
├── views.py               <-- Vistas para home, contacto y registro
└── urls.py                <-- Rutas: '', 'contacto/', 'registro/'



practicas/
│
├── migrations/          <-- (Se crea solo) Historial de cambios en la BD
│
├── static/              <-- Archivos específicos de esta app
│   └── practicas/
│       └── css/         <-- (Opcional) Si quieres estilos solo para el diario
│
├── templates/
│   └── practicas/       <-- IMPORTANTE: Subcarpeta con el nombre de la app
│       ├── lista_entradas.html  <-- Ver tu diario
│       ├── form_entrada.html    <-- Crear/Editar entrada (Crispy Forms)
│       └── lista_empresas.html  <-- Ver empresas y tutores
│
├── admin.py             <-- Para que el profesor vea los datos en el panel
├── apps.py              <-- Configuración (no se toca apenas)
├── forms.py             <-- ¡Clave! Aquí va el ModelForm con Crispy
├── models.py            <-- Ya lo tienes (Empresa, Tutor, EntradaDiario)
├── urls.py              <-- Tus rutas (ej: /diario/nueva)
├── views.py             <-- La lógica (guardar datos, validaciones)
└── tests.py             <-- (No se pide en la rúbrica, puedes ignorarlo)




from django.db import models
from django.contrib.auth.models import User  # Importamos el modelo de usuario de Django




# --- MODELO 1: EMPRESA ---
# Cumple con: CharField y BooleanField [cite: 56]
class Empresa(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la empresa")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono de contacto")
    direccion = models.CharField(max_length=200, verbose_name="Dirección", blank=True, null=True)
    
    # Requisito: BooleanField (Check de si hay convenio)
    convenio_firmado = models.BooleanField(default=True, verbose_name="¿Convenio activo?")

    # Requisito: Método __str__ [cite: 57]
    def __str__(self):
        return self.nombre

# --- MODELO 2: TUTOR ---
# Cumple con: ForeignKey (Relación 1 a N) [cite: 53]
class Tutor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del tutor")
    email = models.EmailField(verbose_name="Correo electrónico", blank=True)
    cargo = models.CharField(max_length=100, verbose_name="Cargo en la empresa", blank=True)
    
    # Relación: Una empresa tiene muchos tutores
    # on_delete=models.CASCADE: Si borras la empresa, se borran sus tutores.
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="tutores")

    def __str__(self):
        return f"{self.nombre} ({self.empresa.nombre})"

# --- MODELO 3: ENTRADA DEL DIARIO ---
# Cumple con: DateField y TextField [cite: 56]
class EntradaDiario(models.Model):
    # Relación: Un alumno tiene muchas entradas
    alumno = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Requisito: DateField
    fecha = models.DateField(verbose_name="Fecha de la práctica")
    
    # Campo numérico para las horas
    horas = models.DecimalField(max_digits=4, decimal_places=2, help_text="Ejemplo: 6.5")
    
    # Requisito: TextField (Texto largo para explicar las tareas)
    tareas = models.TextField(verbose_name="Tareas realizadas")
    
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones / Aprendizaje")
    
    # Campo oculto para ordenar por fecha de creación real
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']  # Ordena las entradas de la más reciente a la más antigua
        verbose_name = "Entrada del Diario"
        verbose_name_plural = "Entradas del Diario"

    def __str__(self):
        return f"Práctica del {self.fecha} - {self.alumno.username}"
        
# --- MODELO 4: ALUMNOS ---   
class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=9)
    ciclo = models.CharField(max_length=50, default="2º DAW")
    
# --- AQUÍ ESTÁN LAS FOREIGN KEYS QUE FALTABAN ---
    
# Relación: Un alumno hace prácticas en UNA empresa

    empresa_asignada = models.ForeignKey(Empresa, on_delete=models.PROTECT, verbose_name="Empresa de FCT")
    
# Relación: Un alumno tiene UN tutor laboral asignado
    tutor_asignado = models.ForeignKey(Tutor, on_delete=models.PROTECT, verbose_name="Tutor Laboral")

    def __str__(self):
        return f"{self.user.username} - {self.empresa_asignada.nombre}"





# from django.db import models

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


# from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio")  # Columnas que se ven
    search_fields = ("nombre",)          # Barra de búsqueda

admin.site.register(Producto, ProductoAdmin)
