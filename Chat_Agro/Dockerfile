# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

ENV OPENAI_API_KEY=sk-t3Wf7uDQEe_7vKPlWJrBL9XO_ypMvs1f2sUidlLtfoT3BlbkFJh_RZ6qGsJP9TYO7lQygZE2wH-59Ka588r2EL3oGxgA

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
