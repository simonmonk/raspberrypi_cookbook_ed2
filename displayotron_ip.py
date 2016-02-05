import dothat.lcd as lcd
import dothat.backlight as backlight
import time
from datetime import datetime
import subprocess

while True:
    lcd.clear()
    backlight.rgb(0, 255, 0)
    try:
        hostname = subprocess.check_output(['hostname']).split()[0]
        ip = subprocess.check_output(['hostname', '-I']).split()[0]
        t = '{:%H:%M:%S}'.format(datetime.now())
        lcd.write(hostname)
        lcd.set_cursor_position(0, 1)
        lcd.write(ip)
        lcd.set_cursor_position(0, 2)
        lcd.write(t)
    except:
        backlight.rgb(255, 0, 0)
    time.sleep(1)