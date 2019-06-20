import RPi.GPIO as GPIO, time,os

intStart = 0
DEBUG = 1
# setup everything for inputs/outputs
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(5, GPIO.OUT) # enable
GPIO.setup(6,GPIO.OUT) # 1A
GPIO.setup(13, GPIO.OUT) #2A
GPIO.setup(4,GPIO.OUT) # 4A
GPIO.setup(19,GPIO.OUT) #3A
GPIO.setup(22,GPIO.OUT) #enable
intValue = GPIO.input(17)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

# start up, press button to power on
while intStart == 0:
        intValue = GPIO.input(17)
        print str(intValue)
        time.sleep(0.5)
        if intValue == 0:
# countdown 5 seconds
                time.sleep(5)
                intStart = 1
                def RCtime (RCpin):
                        reading = 0
                        GPIO.setup(RCpin, GPIO.OUT)
                        GPIO.output(RCpin, GPIO.LOW)
                        time.sleep(0.1)

                        GPIO.setup(RCpin, GPIO.IN)
                        # This takes about 1 millisecond per loop cycle
                        while (GPIO.input(RCpin) == GPIO.LOW):
                                reading += 1
		# Returns light sensor reading to be checked by our if statements
                        return reading

#button pressed
while intStart == 1:
#While light sensor reading is less than 400, continue moving forwards
        if RCtime(23) < 400:
	GPIO.output(5,True)
                GPIO.output(6,True)
                GPIO.output(13,False)
                GPIO.output(22,True)
                GPIO.output(4,True)
                GPIO.output(19,False)
                GPIO.output(21,True)
                GPIO.output(12,False)

#If light sensor ever outputs 400, move back for one second and then turn for one second, then #resume moving forwards
        elif RCtime(23) > 400:
	#backup
                GPIO.output(5,True)
                GPIO.output(6,False)
                GPIO.output(13,True)
                GPIO.output(22,True)
                GPIO.output(4,False)
                GPIO.output(19,True)
                time.sleep(1)
	#turn
                GPIO.output(5, True)
                GPIO.output(6,False)
                GPIO.output(13,True)
                GPIO.output(22,True)
     time.sleep(1)
