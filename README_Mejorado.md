# 📚 Gestión FCT - Sistema de Gestión de Prácticas Profesionales

> **Proyecto desarrollado por:** Basi Córdoba Arcas y Javier Gómez-Comino  
> **Asignatura:** Programación de Aplicaciones Utilizando Frameworks  
> **Curso:** 2º DAW - I.E.S. Juan Bosco

---

## 📋 Descripción del Proyecto

**Gestión FCT** es una aplicación web desarrollada con **Django** que moderniza la gestión tradicional del cuaderno de prácticas en papel. 

La plataforma permite a **alumnos**, **tutores** y **empresas** gestionar de forma digital y centralizada todo el proceso de las prácticas profesionales (FCT), eliminando la necesidad de transportar documentación física entre ciudades.

### 🎯 Funcionalidades principales

- ✅ **Registro de entradas diarias** del cuaderno de prácticas
- ✅ **Gestión de empresas** y tutores laborales
- ✅ **Sistema de autenticación** completo (registro, login, logout)
- ✅ **Área privada** protegida para cada alumno
- ✅ **Formulario de contacto** para consultas
- ✅ **Panel de administración** para profesores

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| **Python 3.x** | Lenguaje de programación |
| **Django 6.0** | Framework web |
| **Bootstrap 5.3** | Framework CSS para diseño responsive |
| **django-crispy-forms** | Renderizado avanzado de formularios |
| **SQLite** | Base de datos (desarrollo) |

---

## 📁 Estructura del Proyecto

```
gestion_fct/
│
├── core/                          # App principal (páginas generales)
│   ├── static/core/
│   │   ├── css/estilos.css       # CSS personalizado
│   │   ├── js/main.js            # JavaScript personalizado
│   │   └── img/logo.png          # Logo y imágenes
│   ├── templates/core/
│   │   ├── base.html             # Plantilla base con Bootstrap
│   │   ├── home.html             # Página de inicio
│   │   └── contacto.html         # Formulario de contacto
│   ├── forms.py                  # ContactoForm (forms.Form)
│   ├── models.py                 # MensajeContacto
│   ├── views.py                  # Vistas de home, contacto, registro
│   └── urls.py                   # Rutas de core
│
├── practicas/                     # App de gestión de prácticas FCT
│   ├── templates/practicas/
│   │   ├── lista_entradas.html   # Ver diario completo
│   │   ├── form_entrada.html     # Crear/editar entrada (Crispy)
│   │   └── lista_empresas.html   # Listado de empresas
│   ├── forms.py                  # EntradaDiarioForm (ModelForm)
│   ├── models.py                 # Empresa, Tutor, Alumno, EntradaDiario
│   ├── views.py                  # Vistas protegidas con @login_required
│   ├── urls.py                   # Rutas de prácticas
│   └── admin.py                  # Panel de administración
│
├── gestion_fct/                   # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py                   # URLs principales
│   └── wsgi.py
│
├── manage.py
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Este archivo
```

---

## 🚀 Instalación y Ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/gestion-fct.git
cd gestion-fct
```

### 2️⃣ Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Realizar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```

Accede a la aplicación en: **http://127.0.0.1:8000/**

---

## 👤 Usuarios de Prueba

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| `alumno1` | `test1234` | Alumno con entradas de diario |
| `admin` | `admin1234` | Superusuario (panel admin) |

> **Nota:** Puedes registrarte como nuevo usuario desde `/registro/`

---

## 📊 Requisitos Técnicos Cumplidos

### ✅ Requisitos Básicos (70%)

| Requisito | Estado | Detalle |
|-----------|--------|---------|
| **2 aplicaciones Django** | ✅ | `core` y `practicas` |
| **3+ modelos** | ✅ | 5 modelos: Empresa, Tutor, Alumno, EntradaDiario, MensajeContacto |
| **Relación ForeignKey** | ✅ | Múltiples relaciones entre modelos |
| **Métodos `__str__()`** | ✅ | Implementados en todos los modelos |
| **2 formularios** | ✅ | `ContactoForm` (Form) y `EntradaDiarioForm` (ModelForm) |
| **Validación de formularios** | ✅ | Con mensajes de error |
| **Autenticación completa** | ✅ | Registro, login, logout |
| **Vista protegida** | ✅ | Diario protegido con `@login_required` |

### ✅ Requisitos Autónomos (30%)

| Requisito | Estado | Detalle |
|-----------|--------|---------|
| **Bootstrap** | ✅ | Integrado en navbar, botones, formularios |
| **Crispy Forms** | ✅ | Usado en formularios con `\|crispy` |
| **Messages framework** | ✅ | Mensajes de éxito/error implementados |
| **Ficheros estáticos** | ✅ | CSS, JS y 3+ imágenes |
| **`{% load static %}`** | ✅ | Implementado correctamente |

---

## 🗂️ Modelos de Datos

### 📌 Modelo: `Empresa`
Representa las empresas colaboradoras donde se realizan las prácticas.

**Campos:**
- `nombre`, `telefono`, `direccion`
- `convenio_firmado` (BooleanField)

### 📌 Modelo: `Tutor`
Tutores laborales asignados en cada empresa.

**Relación:** `ForeignKey` con `Empresa` (1 empresa → N tutores)

### 📌 Modelo: `Alumno`
Estudiantes que realizan prácticas.

**Relaciones:**
- `user` (OneToOne con `User`)
- `empresa_asignada` (ForeignKey con `Empresa`)
- `tutor_asignado` (ForeignKey con `Tutor`)

### 📌 Modelo: `EntradaDiario`
Registro diario de actividades del alumno.

**Campos:**
- `fecha` (DateField), `horas` (DecimalField)
- `tareas` (TextField), `observaciones` (TextField)

**Relación:** `ForeignKey` con `User`

### 📌 Modelo: `MensajeContacto`
Mensajes enviados desde el formulario de contacto.

---

## 🎨 Características Destacadas

### 🔐 Sistema de Autenticación
- Registro de nuevos usuarios
- Inicio y cierre de sesión
- Área privada protegida
- Navbar dinámica según autenticación

### 💬 Messages Framework
- Mensajes de éxito: "Entrada guardada correctamente"
- Mensajes de error: "Error al guardar la entrada"
- Alertas de Bootstrap con cierre automático

### 📝 Formularios con Crispy Forms
- Renderizado automático con Bootstrap
- Validación en cliente y servidor
- Mensajes de error personalizados

### 🎨 Diseño Responsive
- Compatible con móviles, tablets y escritorio
- Navbar colapsable en dispositivos pequeños
- Cards y tablas responsive

---

## 📸 Capturas de Pantalla

*(Añade aquí capturas de pantalla de tu aplicación)*

1. **Página de inicio**
2. **Formulario de entrada al diario**
3. **Lista de entradas del diario**
4. **Panel de administración**

---

## 🔮 Futuras Mejoras

- [ ] Exportación del diario a PDF
- [ ] Notificaciones por email
- [ ] Dashboard con estadísticas de horas
- [ ] Validación de entradas por el tutor
- [ ] Aplicación móvil

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## 👨‍💻 Autores

- **Basi Córdoba Arcas** - [GitHub](#)
- **Javier Gómez-Comino** - [GitHub](#)

---

## 📞 Contacto

¿Tienes dudas o sugerencias? Utiliza el formulario de contacto en la aplicación o envíanos un email.

---

**⭐ Si te ha gustado este proyecto, no olvides darle una estrella en GitHub**
