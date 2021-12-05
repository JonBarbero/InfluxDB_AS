# Imagen base
FROM ubuntu

#Actualizar
RUN apt -qq update -y
RUN apt-get -y upgrade

#Descargar el enviroment
RUN apt install python3-pip -y

RUN apt install virtualenv -y

#Crear el venv (virtualenv)
RUN virtualenv /venv

#Instalar las dependencias de requirements.txt
COPY requirements.txt .

RUN pip install -r requirements.txt

#Ejecutar la app (main.py)
COPY main.py .

CMD ["/usr/bin/python3", "main.py"]