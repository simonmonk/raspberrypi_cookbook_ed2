#!/usr/bin/env python

from oled.device import ssd1306
from oled.render import canvas
from PIL import ImageFont
import time
from datetime import datetime

# Setup Display
device = ssd1306(port=1, address=0x3C)
font_file = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
small_font = ImageFont.truetype('FreeSans.ttf', 12, filename=font_file)
large_font = ImageFont.truetype('FreeSans.ttf', 33, filename=font_file)

# Display a message on 3 lines, first line big font        
def display_message(top_line, line_2):
    global device
    with canvas(device) as draw:
        draw.text((0, 0),  top_line, font=large_font, fill=255)
        draw.text((0, 50),  line_2, font=small_font, fill=255)

while True:
    now = datetime.now()
    date_message = '{:%d %B %Y}'.format(now)
    time_message = '{:%H:%M:%S}'.format(now)
    display_message(time_message, date_message)
    time.sleep(0.1)