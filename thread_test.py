import thread, time, random

def annoy(message):
    while True:
        time.sleep(random.randint(1, 3))
        print(message)
          

thread.start_new_thread(annoy, ('BOO !!',))

x = 0
while True:
    print(x)
    x += 1
    time.sleep(1)