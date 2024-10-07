# Dockerfile para el backend
FROM python:3.12.3-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
#COPY manage.py /app/ 
#COPY ./Prueba_RestAPI /app/  

# Establecer la variable de entorno para Django
ENV DJANGO_SETTINGS_MODULE=Prueba_RestAPI.settings  

# Exponer el puerto para el servidor de desarrollo
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
