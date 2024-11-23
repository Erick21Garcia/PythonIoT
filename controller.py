import paho.mqtt.client as mqtt
import json

BROKER = "localhost"
TOPIC = "home/room/light"

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    value = data["value"]
    accuracy = data["accuracy"]
    
    if value < 50 and accuracy > 0.9:
        print("Encendiendo luces...")
    else:
        print("Apagando luces...")

def main():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER, 1883, 60)
    client.subscribe(TOPIC)
    print("Listening for messages...")
    client.loop_forever()

if __name__ == "__main__":
    main()
