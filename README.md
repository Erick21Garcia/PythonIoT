# PythonIoT

Este proyecto tiene como objetivo explorar el uso del protocolo MQTT en soluciones de Internet de las Cosas (IoT). La práctica incluye la implementación de una simulación para el control automático de iluminación en un entorno doméstico.

## Características principales

- Uso del protocolo MQTT para la comunicación entre dispositivos.
- Simulación de un sensor de luz que publica datos al broker MQTT.
- Controlador de luces que ajusta la iluminación en función de los datos recibidos.
- Opción de simular publicaciones manualmente para pruebas personalizadas.

## Instalación

### Clonar el repositorio

1. Clona el repositorio desde GitHub y accede al directorio del proyecto.
   ```bash
   git clone https://github.com/Erick21Garcia/PythonIoT.git
   cd PythonIoT
   ```

### Instalar dependencias

2. Instala las librerías requeridas ejecutando el siguiente comando en la terminal:
   ```bash
   pip install paho-mqtt uuid
   ```

### Instalar Mosquitto

3. Si no tienes Mosquitto instalado, sigue estos pasos:
   - Abre la terminal y escribe:
     ```bash
     sudo apt update
     sudo apt install mosquitto mosquitto-clients
     ```

### Configurar Mosquitto

4. Inicia el servicio Mosquitto escribiendo en la terminal:
   ```bash
   sudo systemctl start mosquitto
   sudo systemctl enable mosquitto
   ```

## Ejecución

### Paso 1: Iniciar el broker MQTT

Asegúrate de que Mosquitto esté ejecutándose. Para verificarlo, escribe en la terminal:
```bash
sudo systemctl status mosquitto
```

### Paso 2: Ejecutar el publicador (Sensor de luz)

En una terminal, escribe el siguiente comando para iniciar el publicador:
```bash
python sensor.py
```

### Paso 3: Ejecutar el suscriptor (Controlador de luces)

En otra terminal, escribe el siguiente comando para iniciar el suscriptor:
```bash
python controller.py
```

### Paso 4: Simular publicaciones manualmente (opcional)

Si deseas enviar datos al broker manualmente, utiliza el script preparado. Para ello, escribe en la terminal:
```bash
bash publicar.sh
```

## Requisitos del sistema

- Python 3.8 o superior.
- Librerías: `paho-mqtt`, `uuid`.
- Mosquitto instalado y configurado.
- Sistema operativo Linux o cualquier distribución compatible con Mosquitto.
