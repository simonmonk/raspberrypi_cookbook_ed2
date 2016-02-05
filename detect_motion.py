from SimpleCV import *

MIN_BLOG_SIZE = 1000

c = Camera()

old_image = c.getImage()

while True:
    new_image = c.getImage()
    diff = new_image - old_image
    blobs = diff.findBlobs(minsize=MIN_BLOG_SIZE)
    if blobs :
        print("Movement detected")
    old_image = new_image
    print('.')