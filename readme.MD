# Práctica Django: Gestor FCT

**Alumnos:** Basi Córdoba Arcas y Javier Gómez-Comino
**Curso:** 2º DAW
**Instituto:** I.E.S. Juan Bosco

---

## 1. Descripción del proyecto
Este proyecto es nuestra entrega para la práctica de Django. Se trata de una aplicación web diseñada para digitalizar el seguimiento de las Prácticas en Centros de Trabajo (FCT). La idea es que los alumnos puedan llevar su diario de prácticas desde el navegador, apuntando las horas y tareas de cada día, además de guardar la información de la empresa y del tutor asignado.

El código está organizado en dos aplicaciones principales:
* **core:** Se encarga de la estructura base (plantillas genéricas, inicio, quiénes somos), el formulario de contacto y el sistema de registro/login.
* **practicas:** Contiene la lógica principal. Aquí están los modelos de base de datos (`Empresa`, `Tutor` y `RegistroPractica`) y las vistas protegidas para que cada alumno solo vea su propio diario.

A nivel de diseño, hemos utilizado **Bootstrap 5** para que la web sea responsive y **django-crispy-forms** para que los formularios se adapten correctamente a los estilos de Bootstrap.

## 2. Cómo ejecutar el proyecto
Para levantar el proyecto en local, los pasos son los habituales de un entorno de Django:

1. **Activar el entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows: venv\Scripts\activate
   # En Linux/Mac: source venv/bin/activate
Instalar los paquetes necesarios:
Es importante instalar los módulos de Crispy Forms para que los formularios de registro y diario carguen bien.

pip install django django-crispy-forms crispy-bootstrap5
Preparar la base de datos (SQLite):

python manage.py makemigrations
python manage.py migrate
Arrancar el servidor:

python manage.py runserver
La web estará disponible en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 3. Usuarios de prueba
Para que se puedan probar todas las funcionalidades y restricciones (como las vistas protegidas con login), hemos dejado preparados estos dos usuarios:

Usuario Administrador (Profesor):

Usuario: admin

Contraseña: Admin1234

Nota: Este usuario puede entrar a la ruta /admin/ para ver el panel de control, donde hemos personalizado la vista para filtrar fácilmente alumnos y empresas.

Usuario Alumno:

Usuario: basilio

Contraseña: julianalvarez123

Nota: Con este usuario se puede entrar al área privada, registrar entradas en el diario y añadir empresas. 