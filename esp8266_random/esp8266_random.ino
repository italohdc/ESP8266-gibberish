// Using Arduino IDE
// NodeMCU 1.0 (ESP-12E Module), 80MHz, 115200, 4M (1M SPIFFS)

#include <Arduino.h>
#include <ESP8266WiFi.h>

#define LOG(x) Serial.print(x)
#define BAUD_RATE 115200

const char* wifi_ssid = "SSID";
const char* wifi_pass = "PASSWORD";

void setup()
{
	delay(500);
	Serial.begin(BAUD_RATE);
	LOG("\n-- ESP8266 NodeMCU ESP-12E --\n");

	WiFi.begin(wifi_ssid, wifi_pass);

	LOG("\nConnecting to WiFi");
	while (WiFi.status() != WL_CONNECTED) {  
		delay(300);
		LOG(".");
	}
	LOG("\nWiFi connected");
}

void loop()
{
}
