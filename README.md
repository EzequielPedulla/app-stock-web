# App Stock Web

Aplicación web Flask para gestión de inventario con base de datos MySQL.

## 🚀 Características

- ✅ Visualización de productos en tabla
- ✅ Base de datos MySQL
- ✅ Interfaz web moderna con Bootstrap
- ✅ Arquitectura MVC con Blueprints
- ✅ Agregar productos
- ✅ Diseño responsive

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
pip install -r requirements.txt
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
├── requirements.txt       # Dependencias Python
├── .gitignore            # Archivos a ignorar en Git
├── templates/
│   ├── layout.html       # Layout base con Bootstrap
│   ├── index.html        # Lista de productos
│   └── add_product.html  # Formulario agregar producto
├── models/
│   └── products.py       # Modelo Product (SQLAlchemy)
├── routes/
│   └── products_routes.py # Rutas de productos (Blueprint)
└── venv/                 # Entorno virtual
```

## 🔧 Tecnologías utilizadas

- **Python 3.11**
- **Flask 3.1.2**
- **MySQL** con PyMySQL
- **SQLAlchemy** (ORM)
- **Bootstrap 5.3.3** (UI Framework)
- **Jinja2** (Template engine)

## 📈 Próximas funcionalidades

- ✏️ Editar productos existentes
- 🗑️ Eliminar productos
- 🔍 Buscar y filtrar productos
- 📊 Estadísticas de inventario
- 📱 Mejoras en diseño responsive
- 🔐 Sistema de autenticación

## 👨‍💻 Autor

[Tu nombre]

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
