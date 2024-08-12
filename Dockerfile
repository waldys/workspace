# Usar una imagen oficial de Python como base
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY ./miapp.py /app
COPY ./requirements.txt /app

# Instalar las dependencias
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para correr la aplicación
CMD ["uvicorn", "miapp:app", "--host", "0.0.0.0", "--port", "8000"]
