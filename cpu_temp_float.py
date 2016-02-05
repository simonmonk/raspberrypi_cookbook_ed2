import os, time

while True:
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp_s = dev.read()[5:-3] # top and tail string
    cpu_temp = float(cpu_temp_s)
    print(cpu_temp)
    time.sleep(1)