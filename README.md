# 📚 Admin Libros — Taller 2 Django

Aplicación web en Django para gestionar **Autores** y **Libros** con operaciones CRUD completas.

---

## 🗂 Estructura del proyecto

```
admin_libros/
├── manage.py
├── requirements.txt
├── admin_libros/          ← Configuración global
│   ├── settings.py
│   └── urls.py
└── gestion/               ← Aplicación principal
    ├── models.py          ← Modelos Autor y Libro
    ├── forms.py           ← Formularios
    ├── views.py           ← Lógica CRUD
    ├── urls.py            ← Rutas de la app
    ├── admin.py           ← Panel administrativo
    └── templates/gestion/ ← Plantillas HTML
```

---

## ⚙️ Instalación paso a paso

### 1. Crea y activa el entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 2. Instala Django

```bash
pip install -r requirements.txt
```

### 3. Aplica las migraciones (crea la base de datos)

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crea el superusuario (para el panel /admin)

```bash
python manage.py createsuperuser
```
Escribe un nombre de usuario, correo y contraseña cuando te los pida.

### 5. Ejecuta el servidor

```bash
python manage.py runserver
```

---

## 🌐 URLs disponibles

| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000/` | Redirige a lista de autores |
| `http://127.0.0.1:8000/autores/` | Lista de autores |
| `http://127.0.0.1:8000/autores/crear/` | Crear autor |
| `http://127.0.0.1:8000/autores/editar/<id>/` | Editar autor |
| `http://127.0.0.1:8000/autores/eliminar/<id>/` | Eliminar autor |
| `http://127.0.0.1:8000/libros/` | Lista de libros |
| `http://127.0.0.1:8000/libros/crear/` | Crear libro |
| `http://127.0.0.1:8000/libros/editar/<id>/` | Editar libro |
| `http://127.0.0.1:8000/libros/eliminar/<id>/` | Eliminar libro |
| `http://127.0.0.1:8000/admin/` | Panel de administración Django |

---

## 🗄 Modelos

### Autor
| Campo | Tipo | Descripción |
|-------|------|-------------|
| nombre | CharField | Nombre completo |
| correo | EmailField | Correo único |
| nacionalidad | CharField | Nacionalidad |
| fecha_nacimiento | DateField | Fecha de nacimiento |
| biografia | TextField | Biografía (opcional) |

### Libro
| Campo | Tipo | Descripción |
|-------|------|-------------|
| titulo | CharField | Título del libro |
| fecha_publicacion | DateField | Fecha de publicación |
| genero | CharField | Género literario |
| isbn | CharField | ISBN único |
| autor | ForeignKey | Relación con Autor |

> Un **Autor** puede tener muchos **Libros** (relación 1 a N).  
> Si eliminas un autor, también se eliminan todos sus libros.

---

## 💡 Notas

- La base de datos es **SQLite** (archivo `db.sqlite3`) — no necesitas instalar nada extra.
- Los formularios usan **Bootstrap 5** cargado desde CDN (necesitas internet).
- Para cambiar el idioma o zona horaria edita `settings.py` → `LANGUAGE_CODE` y `TIME_ZONE`.
