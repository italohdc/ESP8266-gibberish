import tkinter
from tkinter import *#messagebox
# from tkinter import font
import mqtt_receiver as mqtt

window = tkinter.Tk()
window_width=420
window_height=240
update_delay = 60

black_lvl = 0
window_color = '#%02x%02x%02x' % (black_lvl, black_lvl, black_lvl)

def black_level(level):
	global black_lvl; global window_color
	black_lvl = level
	if black_lvl<0: black_lvl=0
	if black_lvl>255 : black_lvl=255
	window_color = '#%02x%02x%02x' % (black_lvl, black_lvl, black_lvl)

my_canvas = tkinter.Canvas(window, bg=window_color, height=window_height, width=window_width, cursor='dot')

textbox_xy = [[20,20],[20,60],[100,60],[100,20]]
textbox = my_canvas.create_polygon(textbox_xy, fill='white')

text_xy = [60,40]
# text_font = ('Helvetica', 36, 'italic')
text = my_canvas.create_text(text_xy, fill="black")

def range_black(lvl):
	return int(lvl*0.2493)

def update():
	sensor = mqtt.read_topic()
	black_level( range_black(sensor) )

	my_canvas.itemconfig(text, text=str(sensor))
	my_canvas.config(bg=window_color)
	my_canvas.after(update_delay, update)

my_canvas.pack()
my_canvas.after(update_delay, update)
window.mainloop()





# set_black_level(0)
# my_canvas = tkinter.Canvas(window, bg=window_color, height=window_height, width=window_width, cursor='dot')

# my_canvas.pack()
# window.mainloop()
