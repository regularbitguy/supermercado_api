# Supermercado API

API REST desarrollada con **Django + Django REST Framework + MySQL** para gestionar un sistema de supermercado.

---

## Requisitos

- Python 3.10+
- Django 5.x
- Django REST Framework
- MySQL
- pip (gestor de paquetes de Python)
- Git

---

Instalación

1. **Crear un entorno virtual**
   ```
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate      # En Windows
   ```
2. **Instalar dependencias**
   ```
   pip install -r requirements.txt
   ```
3. **Crear la base de datos**
   ```
   CREATE DATABASE supermercado_db;
   ```
4. **Configurar la base de datos MySQL**
   ```
   DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'supermercado_db',
         'USER': 'root',
         'PASSWORD': 'tu_contraseña',
         'HOST': 'localhost',
         'PORT': '3306',
     }
   }
   ```
5. **Migrar la base de datos**
   ```
   python manage.py migrate
   ```
6. **Levantar el servidor**
   ```
   python manage.py runserver
   ```

7 **📡 Endpoints principales**

```
GET /api/productos/ = Lista de productos

GET /api/productos/{id}/ = Detalle de producto

POST /api/productos/ = Crear producto

PUT /api/productos/{id}/ = Editar producto

DELETE /api/productos/{id}/ = Eliminar producto
```
