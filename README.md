# App Stock Web

Aplicación web Flask para gestión de inventario con base de datos SQLite.

## 🚀 Características

- ✅ Visualización de productos en tabla
- ✅ Base de datos SQLite local
- ✅ Interfaz web simple y funcional
- ✅ Arquitectura MVC preparada para expansión

## 📊 Datos de ejemplo

La aplicación incluye productos de ejemplo:

- **Oreo**: Precio $900, Stock: 77
- **Pepas**: Precio $9000, Stock: 7996

## 🛠️ Instalación

1. **Clonar el repositorio:**

```bash
git clone https://github.com/TU_USUARIO/app-stock-web.git
cd app-stock-web
```

2. **Crear entorno virtual:**

```bash
python -m venv venv
```

3. **Activar entorno virtual:**

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. **Instalar dependencias:**

```bash
pip install -r requiments.txt
```

5. **Ejecutar aplicación:**

```bash
python app.py
```

6. **Abrir navegador:**

```
http://127.0.0.1:5000
```

## 📁 Estructura del proyecto

```
app-stock-web/
├── app.py                 # Aplicación principal Flask
├── config.py              # Configuración de base de datos
├── requiments.txt         # Dependencias Python
├── database/
│   └── inventory.db       # Base de datos SQLite
├── templates/
│   └── index.html         # Template HTML principal
├── models/                # Modelos SQLAlchemy (preparado)
├── routes/                # Rutas Flask (preparado)
└── venv/                  # Entorno virtual
```

## 🔧 Tecnologías utilizadas

- **Python 3.11**
- **Flask 3.1.2**
- **SQLite3**
- **Jinja2** (Template engine)
- **HTML/CSS**

## 📈 Próximas funcionalidades

- ➕ Agregar productos
- ✏️ Editar productos existentes
- 🗑️ Eliminar productos
- 🔍 Buscar productos
- 📊 Estadísticas de inventario
- 🎨 Mejoras en el diseño CSS

## 👨‍💻 Autor

[Tu nombre]

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
