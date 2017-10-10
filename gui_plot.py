import numpy as np
import matplotlib.pyplot as plt
import mqtt_receiver as mqtt

sensor = [0] * 50
# sensor[0] = 1024

plt.ion()

while True:
	plt.axis([0, len(sensor), 0, 1024])
	sensor[0] = mqtt.read_topic()
	for x in xrange(len(sensor)-1, 0, -1):
		sensor[x] = sensor[x-1]
		# print(sensor[x],sensor[x-1])
	# print(sensor)
	for i in range(len(sensor)):
	    y = np.random.random()
	    plt.scatter(i, sensor[i])
	    # plt.pause(0.0005)
	plt.pause(0.000001)
	plt.clf()

#     plt.pause(0.05)




# import matplotlib.pyplot as pyplot
# import time


# pyplot.ion()
# fig = pyplot.figure()
# fig.plot(sensor)
# pyplot.ylabel('LDR sensor')
# # pyplot.show()

# while True:
# 	sensor[0] = mqtt.read_topic()
# 	print(sensor)
# 	pyplot.plot(sensor)
# 	time.sleep(0.4)
# 	pyplot.clf()

# import matplotlib.pyplot as plt
# import mqtt_receiver as mqtt
# import numpy as np

# sensor = [0] * 30
# sensor[0] = 1024

# x = np.linspace(0, 6*np.pi, 100)
# y = np.sin(x)

# # You probably won't need this if you're embedding things in a tkinter plot...
# plt.ion()

# fig = plt.figure()
# ax = fig.add_subplot(111)
# line1 = ax.plot(1, 2, 'r-') # Returns a tuple of line objects, thus the comma

# # for phase in np.linspace(0, 10*np.pi, 500):
# while True:
#     line1.set_ydata(mqtt.read_topic())
#     fig.canvas.draw()

# # 	sensor[0] = mqtt.read_topic()
# # 	for x in xrange(1,len(sensor)):
# # 		sensor[x] = sensor[x-1]
# # 	print(sensor)
# # 	plt.plot(sensor)
# # 	plt.clf()
# # 	time.sleep(0.4)