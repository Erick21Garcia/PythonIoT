# PythonIoT
Esta práctica tiene como objetivo explorar el uso del protocolo MQTT en soluciones de Internet de las Cosas (IoT), implementando una simulación de control automático de iluminación en un entorno doméstico.

Instalación
Clonar el repositorio:
Es necesario clonar el repositorio desde GitHub y acceder al directorio del proyecto.
Escribe el siguiente comando en la terminal:
Git clone seguido de la dirección del repositorio, por ejemplo:

git clone https://github.com/Erick21Garcia/PythonIoT.git
cd tu_repositorio
Instalar dependencias:
Instalar las librerías requeridas ejecutando el siguiente comando en la terminal:

pip install paho-mqtt uuid
Instalar Mosquitto:
Si no tienes Mosquitto instalado, sigue estos pasos:

Abre la terminal y escribe:
sudo apt update
sudo apt install mosquitto mosquitto-clients
Configurar Mosquitto:
Inicia el servicio Mosquitto escribiendo en la terminal:

sudo systemctl start mosquitto
sudo systemctl enable mosquitto
Ejecución
Paso 1: Iniciar el broker MQTT
Asegúrate de que Mosquitto esté ejecutándose. Para verificarlo, escribe en la terminal:

sudo systemctl status mosquitto
Paso 2: Ejecutar el publicador (Sensor de luz)
En una terminal, escribe el siguiente comando para iniciar el publicador:

python sensor.py
Paso 3: Ejecutar el suscriptor (Controlador de luces)
En otra terminal, escribe el siguiente comando para iniciar el suscriptor:

python controller.py
Paso 4: Simular publicaciones manualmente (opcional)
Si deseas enviar datos al broker manualmente, utiliza el script preparado. Para ello, escribe en la terminal:

bash publicar.sh
