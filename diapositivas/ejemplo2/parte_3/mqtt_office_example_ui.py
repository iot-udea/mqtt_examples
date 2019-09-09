import paho.mqtt.client as mqtt
import time
from tkinter import *


class LampControlUI(Frame):
    def __init__(self,master = None):
        Frame.__init__(self, master)
        self.pack()

        # Variables asociadas al cliente mqtt
        self.ledState = False
        self.broker_IP = "192.168.1.11"
        self.topics = ["home/office/lamp"]
        self.commands = ["ON","OFF"]

        # cliente mqtt
        CLIENT_ID = "lis01"
        self.mqttc=mqtt.Client(client_id=CLIENT_ID)
        self.mqttc.connect(self.broker_IP, 1883, 60)


        # Agregando frames principales
        self.buttonLamp = Button(self,text="ON",command = self.on_off_light)
        self.buttonLamp.pack(side=LEFT)
        self.ledLabel = Label(self,text = "Lampara Apagada")
        self.ledLabel.pack(side=LEFT)

        # Iniciando el loop infinito del cliente mqtt
        self.mqttc.loop_start() 


    def on_off_light(self):
        if self.ledState == False:
            #self.ser.write('h'.encode("ascii","ignore")) #envia la entrada por serial
            self.buttonLamp.config(text = "ON")
            self.ledLabel.config(text = "Lampara apagada")
            self.mqttc.publish(self.topics[0],self.commands[0])  # Uso de publish para prender la lampara
            self.ledState = True
        else:
            #self.ser.write('l'.encode("ascii","ignore"))
            self.buttonLamp.config(text = "OFF")
            self.mqttc.publish(self.topics[0],self.commands[1])  # Uso de publish para apagar la lampara
            self.ledLabel.config(text = "Lampara encendida")
            self.ledState = False

# Allow the class to run stand-alone.
if __name__ == "__main__":
    app = LampControlUI()
    app.mainloop()


