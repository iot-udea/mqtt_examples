import paho.mqtt.client as mqtt
import time


# Variables de la aplicacion
BROKER_IP = "192.168.1.11"
TOPIC = "home/office/lamp"
LAMP_ON = "ON"
LAMP_OFF = "OFF"

# 1. Creacion de la isntanca del cliente
CLIENT_ID = "lis01"
mqtt_client=mqtt.Client(client_id=CLIENT_ID)

# 2. Incovacion del metodo connect
mqtt_client.connect(BROKER_IP, 1883, 60)

# 3. Llamando el loop para mantener el flujo de trafico de red en el broker
# 4. No se llevo a cabo en este caso.
mqtt_client.loop_start()
print("SISTEMA DE CONTROL DE LA LAMPARA DE LA OFFICE")
while True:
  print("Menu de control de la office " )
  print("1. Encender lampara" )
  print("2. Apagar lampara" )
  print("3. Salir de la aplicacion" )
  opc = input("Seleccione una opcion: ")
  if opc == '1':
      print("--> Encendiendo la lampara\n")
      mqtt_client.publish(TOPIC,LAMP_ON)  # Uso de publish para prender la lampara
  elif opc == '2':
      print("--> Apagando la lampara\n")
      mqtt_client.publish(TOPIC,LAMP_OFF) # Uso de publish para apagar la lampara
  elif opc == '3':
      print("--> Chao bambino\n")
      break
  else:
      print("--> OPCION INVALIDA\n")
mqtt_client.loop_stop()