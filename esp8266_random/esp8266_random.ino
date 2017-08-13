// Using Arduino IDE
// NodeMCU 1.0 (ESP-12E Module), 80MHz, 115200, 4M (1M SPIFFS)
//#include "lelis.h"

#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define LOG(x) Serial.print(x)
#define BAUD_RATE 115200

#define PIN_BUILTIN_LED 2
#define PIN_LDR A0

const char* wifi_ssid = "SSID";
const char* wifi_pass = "PASSWORD";
const char* mqtt_server = "broker.hivemq.com";//"broker.mqtt-dashboard.com";
const uint16_t mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

void setup()
{
	delay(500);
	Serial.begin(BAUD_RATE);
	LOG("\n-- ESP8266 NodeMCU ESP-12E --\n");

	pinMode(PIN_BUILTIN_LED, OUTPUT);
	setup_wifi();
	setup_mqtt();
	LOG("\n");
}

void setup_wifi ()
{
	WiFi.begin(wifi_ssid, wifi_pass);
	LOG("\nConnecting to WiFi");
	while (WiFi.status() != WL_CONNECTED) {
		digitalWrite(PIN_BUILTIN_LED, !HIGH);
		delay(500); 	LOG(".");
		digitalWrite(PIN_BUILTIN_LED, !LOW);
	}
	LOG("\nWiFi connected");
	LOG("\nLocal IP Address: ");
	LOG(WiFi.localIP());
}

void setup_mqtt ()
{
	client.setServer(mqtt_server, mqtt_port);
	client.setCallback(mqtt_callback);
	mqtt_connect();
}

void mqtt_callback(char* topic, byte* payload, unsigned int length) {
  LOG("\nMessage arrived [");
  LOG(topic);
  LOG("] ");
  for (int i = 0; i < length; i++) {
    LOG((char)payload[i]);
  }
}

void mqtt_connect ()
{
	while( !client.connected() )
	{
		LOG("\nAttempting MQTT connection...");
		if(client.connect("ESP8266-gibberish"))
		{
			LOG("connected");
			client.publish("ESP8266-gibberish/connection status", "Connected!");
			LOG("\nConnected and sent!");
		}
		delay(5000);
	}
}

uint16_t read_ldr ()
{
	return analogRead(PIN_LDR);
}

void loop()
{
	if( !client.connected() ) mqtt_connect();
	client.loop();
}
