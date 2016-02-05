# 08_manual_robot.py
# Use the arrow keys to direct the robot

from rrb3 import *
import sys
import tty
import termios

rr = RRB3(9.0, 6.0) # battery, motor

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

print("Use the arrow keys to move the robot")
print("Press CTRL-c to quit the program")

# These functions allow the program to read your keyboard
def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

# This will control the movement of your robot and display on your screen
try: 
    while True:
        keyp = readkey()
        if keyp == UP:
            rr.forward(1)
            print 'forward'
        elif keyp == DOWN:
            rr.reverse(1)
            print 'backward'
        elif keyp == RIGHT:
            rr.right(1)
            print 'clockwise'
        elif keyp == LEFT:
            rr.left(1)
            print 'anti clockwise'
        elif keyp == LEFT:
            rr.left(1)
            print 'anti clockwise'   
        elif ord(keyp) == 3:
            break

except KeyboardInterrupt:
    GPIO.cleanup()

