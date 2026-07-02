# CRUD Empleados y Cargos — Vistas Basadas en Funciones (VBF)

Etapa 1 del proyecto. CRUD completo de **Cargos** y **Empleados** usando
Vistas Basadas en Funciones (function-based views).

## Modelos

- **Cargo**: `nombre`, `descripcion`.
- **Empleado**: `nombres`, `apellidos`, `correo`, `sueldo`, `fecha_ingreso`,
  `cargo` (ForeignKey → Cargo). Un cargo tiene muchos empleados; cada empleado
  pertenece a un solo cargo. El campo `cargo` se muestra como lista desplegable.

## Estructura

- `gestion/` — configuración del proyecto (settings, urls).
- `personal/` — app con `models.py`, `forms.py`, `views.py` (funciones),
  `urls.py`, `admin.py`, `migrations/` y `templates/`.

## Cómo ejecutar

```bash
py -m venv env
env\Scripts\activate          # Windows
pip install -r requirements.txt
py manage.py migrate
py manage.py runserver
```

Abrir http://127.0.0.1:8000/

## Rutas

| URL | Acción |
|-----|--------|
| `/cargos/` | Listar cargos |
| `/cargos/nuevo/` | Crear cargo |
| `/cargos/<id>/editar/` | Editar cargo |
| `/cargos/<id>/eliminar/` | Eliminar cargo |
| `/empleados/` | Listar empleados |
| `/empleados/nuevo/` | Crear empleado |
| `/empleados/<id>/editar/` | Editar empleado |
| `/empleados/<id>/eliminar/` | Eliminar empleado |
"# EMPLEADOS_VBF" 
