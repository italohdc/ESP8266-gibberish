# ESP8266-gibberish
Doing gibberish stuff with an ESP8266

> For Arduino IDE: NodeMCU 1.0 (ESP-12E Module), 80MHz, 115200, 4M (**1M** SPIFFS)

## ESP8266 Random

Read value from LDR on ESP8266 and send it to a broker using MQTT.

Code in Python subscribe to MQTT topic and send values to a GUI, which prints the given value and change the background color accordingly.

## Libraries

In the ESP code:

>\#include <[PubSubClient.h](https://github.com/knolleary/pubsubclient)>

In the Python code:

>import [paho.mqtt.client](https://pypi.python.org/pypi/paho-mqtt/1.1)

>import [tkinter](https://wiki.python.org/moin/TkInter)

### Errors found

* ~~For some reason, when using Serial Monitor on Arduino IDE, the information sent through ``Serial.print("Lorem Ipsum")`` only start printing after some write was made (not sure yet if after any x characters or after x ``\n`` characters).~~
* Uploading firmware works better when using 1M Flash. (And also solves the above problem) 🤷‍♂️
* Couldn't convert int to char* (not String) using any bult-in method (like ``.toCharArray``, ``String(parameter``, ``sprintf(...)``)). Trying to use a separated function to handle it.
* On the above issue, note to future self: if you're using C, not py, don't use char*, use char [10].

---

``Definition of I. for Broker: "Pior ainda, tudo que você for fazer com ele, estará quebrado"``


``>> Enquanto fazia pão de queijo``
