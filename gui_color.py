import tkinter
from tkinter import *#messagebox
import mqtt_receiver as mqtt

window = tkinter.Tk()
window_width=1024
window_height=768
update_delay = 1

black_lvl = 0
window_color = '#%02x%02x%02x' % (black_lvl, black_lvl, black_lvl)

def black_level(level):
	global black_lvl; global window_color
	black_lvl = level
	if black_lvl<0: black_lvl=0
	if black_lvl>255 : black_lvl=255
	window_color = '#%02x%02x%02x' % (black_lvl, black_lvl, black_lvl)

my_canvas = tkinter.Canvas(window, bg=window_color, height=window_height, width=window_width, cursor='dot')

textbox_xy = [[50,50],[50,200],[500,200],[500,50]]
textbox = my_canvas.create_polygon(textbox_xy, fill='white')
	#my_canvas.itemconfig(textbox, fill='blue')

# text_xy = [60,60]
# text = tkinter.Text(window, height=100, width=30)
# text.insert(INSERT, "Hello World!")

def range_black(lvl):
	return int(lvl*0.2493)

def update():

	black_level( range_black(mqtt.read_topic()) )

	my_canvas.config(bg=window_color)
	my_canvas.after(update_delay, update)

my_canvas.pack()
my_canvas.after(update_delay, update)
window.mainloop()





# set_black_level(0)
# my_canvas = tkinter.Canvas(window, bg=window_color, height=window_height, width=window_width, cursor='dot')

# my_canvas.pack()
# window.mainloop()
