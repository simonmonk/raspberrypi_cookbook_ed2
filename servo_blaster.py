from Tkinter import *
import os
import time

servo_min = 500  # uS
servo_max = 2500  # uS

servo = 2 # GPIO 18
  
def map(value, from_low, from_high, to_low, to_high): 
  from_range = from_high - from_low
  to_range = to_high - to_low
  scale_factor = float(from_range) / float(to_range)
  return to_low + (value / scale_factor)
  
  
def set_angle(angle):
  pulse = int(map(angle, 0, 180, servo_min, servo_max))
  command = "echo {}={}us > /dev/servoblaster".format(servo, pulse)
  os.system(command)
  
    
class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        set_angle(float(angle))

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()