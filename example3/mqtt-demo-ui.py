import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
from tkinter import *


class LampControlUI(Frame):

    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.pack()


        self.broker_IP = "192.168.1.11"

        # Agregando frames principales
        self.alarmLabel = Label(self,text = "Temperatura normal")
        self.alarmLabel.pack()
        self.ledLabel = Label(self,text = "T: ")
        self.ledLabel.pack()

        # cliente mqtt
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker_IP, 1883, 60)
        print("connecting")

        # Iniciando el loop infinito del cliente mqtt
        self.client.loop_start() 
         
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+ str(rc))
        self.client.subscribe("casa/#")

    def on_message(self, client, userdata, msg):
        print("We got a message")
        print('%s %s' % (msg.topic, msg.payload))
        if float(msg.payload) > 260:
          print("ALERTA")
          publish.single("casa/despacho/luz", "1", hostname=self.broker_IP)

# Allow the class to run stand-alone.
if __name__ == "__main__":
    app = LampControlUI()
    app.mainloop()


