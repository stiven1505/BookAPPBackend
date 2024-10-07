 Backend - Django REST API

Este proyecto es el backend de la aplicación. Está desarrollado usando **Django** y **Django REST Framework**.

## Estructura de la carpeta
Prueba_RestAPI/ │ ├── books/ # Aplicación Django con lógica del modelo y vistas ├── Prueba_RestAPI/ # Configuraciones del proyecto ├── manage.py # Script de Django para administrar el proyecto ├── requirements.txt # Dependencias de Python └── Dockerfile # Dockerfile para producción

## Configuración del entorno

### Variables de entorno

Asegúrate de configurar las siguientes variables de entorno en un archivo `.env` (o en las variables de tu entorno de despliegue):

- `DEBUG`: `False` en producción
- `ALLOWED_HOSTS`: Lista de hosts permitidos

### Iniciar en modo desarrollo

1. Clona el repositorio y ve a la carpeta del backend:
   ```bash
   git clone https://github.com/tu-usuario/nombre-repositorio.git
   cd Prueba_RestAPI

2.Crea un entorno virtual e instala las dependencias:
  python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
pip install -r requirements.txt

3.Realiza las migraciones de la base de datos:
python manage.py migrate

4.Inicia el servidor de desarrollo:
python manage.py runserver

El backend estará disponible en http://localhost:8000/.

Ejecutar en Docker (Producción)
1.Construye la imagen Docker:
docker build -t nombre-backend .

2.Ejecuta el contenedor:
docker run -p 8000:8000 nombre-backend

