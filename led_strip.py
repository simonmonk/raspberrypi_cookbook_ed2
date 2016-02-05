import time
from neopixel import *

# LED strip configuration:
LED_COUNT      = 10      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

RED = Color(255, 0, 0)
NO_COLOR = Color(0, 0, 0)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

def clear():
	for i in range(0, LED_COUNT):
		strip.setPixelColor(i, NO_COLOR)
	strip.show()

i = 0
while True:
	clear()
	strip.setPixelColor(i, RED)
	strip.show()
	time.sleep(1)
	i += 1
	if i >= LED_COUNT:
		i = 0