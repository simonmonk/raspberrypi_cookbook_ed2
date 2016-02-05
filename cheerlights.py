from squid import *
import urllib, time

squid = Squid(18, 23, 24)
cheerlights_url = "http://api.thingspeak.com/channels/1417/field/2/last.txt"


try:
    while True:
        try:
            cheerlights = urllib.urlopen(cheerlights_url) 
            c = cheerlights.read()             
            cheerlights.close()                           
            print(c)                    
            squid.set_color_rgb(c)
        except:
            print('Error')
        time.sleep(2)
        
finally: 
    GPIO.cleanup()
    