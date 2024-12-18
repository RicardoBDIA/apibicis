# Usar una imagen base de Python
FROM python:3.10

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar el script
CMD ["python", "scripts/recolector.py"]
