import picamera
from SimpleCV import *

def get_camera_image():
    with picamera.PiCamera() as camera:
        camera.capture('tmp.jpg')
    return Image('tmp.jpg')
            
while True:
    i = get_camera_image().invert()
    coins = i.findCircle(canny=100, thresh=70, distance=15)
    print(len(coins))