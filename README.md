# ESP8266-gibberish
Doing gibberish stuff with a ESP8266

> For Arduino IDE: NodeMCU 1.0 (ESP-12E Module), 80MHz, 115200, 4M (1M SPIFFS)

## ESP8266 Random

### Errors found

* For some reason, when using Serial Monitor on Arduino IDE, the information sent through ``Serial.print("Lorem Ipsum")`` only start printing after some write was made (not sure yet if after any x characters or after x ``\n`` characters).
* For some reason, uploading firmware works better when using 1M Flash. (And also solves the above problem) 🤷‍♂️

```Enquanto fazia pão de queijo```