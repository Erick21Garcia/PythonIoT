import paho.mqtt.client as mqtt
import json
import time
import uuid
from datetime import datetime

BROKER = "localhost"
TOPIC = "home/room/light"

def publish_sensor_data():
    client = mqtt.Client()
    client.connect(BROKER, 1883, 60)
    
    device_id = str(uuid.uuid4())
    while True:
        data = {
            "device_id": device_id,
            "event_time": str(datetime.now()),
            "value": 60,  # Cambiar este valor para probar el comportamiento
            "accuracy": 0.98
        }
        client.publish(TOPIC, json.dumps(data))
        print(f"Data sent: {data}")
        time.sleep(5)

if __name__ == "__main__":
    publish_sensor_data()
