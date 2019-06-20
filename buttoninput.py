import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)


intloop = 1


while intloop == 1:
        intValue =GPIO.input(17)
        print str(intValue)
        time.sleep(0.5)
