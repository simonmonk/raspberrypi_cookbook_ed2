#!/usr/bin/env python
import time
import dweepy
import RPi.GPIO as GPIO

KEY = 'tweet_about_me'
OUTPUT_PIN = 18
OUTPUT_DURATION = 10


GPIO.setmode(GPIO.BCM)
GPIO.setup(OUTPUT_PIN, GPIO.OUT)

while True:
    try:
        for dweet in dweepy.listen_for_dweets_from(KEY):
            print('Tweet: ' + dweet['content']['text'])
            GPIO.output(OUTPUT_PIN, True)
            time.sleep(OUTPUT_DURATION)
            GPIO.output(OUTPUT_PIN, False)
    except Exception:
        pass
