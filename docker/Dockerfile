# Imagen base
FROM ubuntu

#Actualizar
RUN apt-get -y update
RUN apt-get -y upgrade

#Python3
RUN apt install python3-pip -y

#Preparar el directorio docker
COPY main.py /docker/main.py
COPY sleep.sh /docker/sleep.sh
COPY requirements.txt /docker/requirements.txt
WORKDIR /docker

#Actualizar pip
RUN pip install --upgrade pip

#Instalar requirements.txt
RUN python3 -m pip install -r requirements.txt

#Permisos a sleep.sh
RUN chmod 777 sleep.sh

#Comando de inicio
CMD ./sleep.sh