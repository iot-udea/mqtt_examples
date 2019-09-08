/*
  Basic ESP8266 MQTT example

  This sketch demonstrates the capabilities of the pubsub library in combination
  with the ESP8266 board/library.

  It connects to an MQTT server then:
  - publishes "hello world" to the topic "outTopic" every two seconds
  - subscribes to the topic "inTopic", printing out any messages
    it receives. NB - it assumes the received payloads are strings not binary
  - If the first character of the topic "inTopic" is an 1, switch ON the ESP Led,
    else switch it off

  It will reconnect to the server if the connection is lost using a blocking
  reconnect function. See the 'mqtt_reconnect_nonblocking' example for how to
  achieve the same result without blocking the main loop.

  To install the ESP8266 board, (using Arduino 1.6.4+):
  - Add the following 3rd party board manager under "File -> Preferences -> Additional Boards Manager URLs":
       http://arduino.esp8266.com/stable/package_esp8266com_index.json
  - Open the "Tools -> Board -> Board Manager" and click install for the ESP8266"
  - Select your ESP8266 in "Tools -> Board"

*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h> //This library provides a client for doing simple publish/subscribe messaging with a server that supports MQTT
//https://pubsubclient.knolleary.net/api.html --> documentation

#define BUILTIN_LED 2
// Update these with values suitable for your network.
const char* ssid = "Ramirez_Bo";                 // Modificar
const char* password = "22081985";               // Modificar
const char* mqtt_server = "192.168.1.8";       // Modificar

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
float value = 0.5;

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.disconnect();
  delay(100);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    Serial.print(WiFi.status());
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
/**
 * If the client is used to subscribe to topics, a callback function must be provided in the constructor. 
 * This function is called when new messages arrive at the client.
 */
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

/*   digitalWrite(BUILTIN_LED, LOW);
   delay(1000);
   digitalWrite(BUILTIN_LED, HIGH);
   delay(1000);
*/   
  // Switch on the LED if an 1 was received as first character
   if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("casa/despacho/temperatura", "Enviando el primer mensaje");
      // ... and resubscribe
      client.subscribe("casa/despacho/luz");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis(); //devuelve el número de milisegundos desde que Arduino se ha reseteado
  if (now - lastMsg > 2000) {
    lastMsg = now;
    value += 1.0;
    snprintf (msg, 75, "%.2f ", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("casa/despacho/temperatura", msg);
  }
}
