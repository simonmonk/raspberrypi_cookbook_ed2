from rrb3 import *
import time

rr = RRB3(12.0, 12.0) # battery, motor

try: 
    while True:
        delay = raw_input("Delay between steps (milliseconds)?")
        steps = raw_input("How many steps forward? ")
        rr.step_forward(int(delay) / 1000.0, int(steps))
        steps = raw_input("How many steps backwards? ")
        rr.step_reverse(int(delay) / 1000.0, int(steps))

finally:
    GPIO.cleanup()