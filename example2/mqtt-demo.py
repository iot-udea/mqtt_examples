import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("casa/#")

def on_message(client, userdata, msg):
    print("We got a message")
    print('%s %s' % (msg.topic, msg.payload))
    if float(msg.payload) > 260:
        print("ALERTA")
        publish.single("casa/despacho/luz", "1", hostname='127.0.0.1')
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
print("connecting")

run = True
while run:
        client.loop()

#client.loop_forever()
