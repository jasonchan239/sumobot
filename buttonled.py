import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(17,GPIO.IN)

intCount  = 1

while intCount ==1:
        intValue = GPIO.input(17)
        if intValue == 1:
                GPIO.output(21,True)
                GPIO.output(12,False)
                time.sleep(0.25)
        elif intValue == 0:
                GPIO.output(12,True)
                GPIO.output(21,False)
                time.sleep(0.25)
