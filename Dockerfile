# Utilizamos una imagen oficial de Python
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos para instalar las dependencias
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el archivo HDF5 al contenedor
COPY SMAP_L4_SM_aup_20240926T030000_Vv7031_001.h5 /app/data/

# Copiamos el código de la aplicación FastAPI en el contenedor
COPY . .

# Exponemos el puerto 8000 para acceder a la API
EXPOSE 8000

# Comando para ejecutar el servidor Uvicorn de FastAPI
CMD ["uvicorn", "api_humedad:app", "--host", "0.0.0.0", "--port", "8000"]