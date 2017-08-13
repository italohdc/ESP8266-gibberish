import paho.mqtt.client as mqtt

# message = ""

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	# client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
	# print(msg.topic+" "+str(msg.payload))
	# print(str(msg.payload))
	global received, message
	message = str(msg.payload)
	received=True

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.mqtt-dashboard.com", 1883, 60)
client.subscribe("ESP8266-gibberish/sensors/ldr")


def read_topic():
	global received, message
	received = False

	while(not received):
		client.loop()

	delete = "b'@"
	for char in delete: message = message.replace(char, "")
	print("LDR:", message, "\n")
	return int(message)

# read_topic()
# while 1: read_topic()