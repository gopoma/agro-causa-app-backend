# Utilizamos una imagen oficial de Python slim
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos para instalar las dependencias
COPY requirements.txt .

# Instalamos las dependencias de manera eficiente
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la aplicación FastAPI en el contenedor
COPY ./src /app/src

# Exponemos el puerto 8000 para acceder a la API
EXPOSE 8000

# Comando para ejecutar el servidor Uvicorn de FastAPI
CMD ["uvicorn", "src.api_humedad:app", "--host", "0.0.0.0", "--port", "8000"]
