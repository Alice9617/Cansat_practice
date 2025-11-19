import RPi.GPIO as GPIO
import time
LED=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,True)
time.sleep(5)
GPIO.output(LED,False)
GPIO.cleanup()
