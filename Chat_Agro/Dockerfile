# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

ENV OPENAI_API_KEY=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

# Copiar el archivo de dependencias
COPY requirements.txt requirements.txt

# Instalar las dependencias dentro del contenedor
RUN pip install -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . .

RUN python create_db.py

# Exponer el puerto en el que correrá la aplicación
EXPOSE 5000

# Definir el comando para iniciar la aplicación
CMD ["python", "app.py"]
