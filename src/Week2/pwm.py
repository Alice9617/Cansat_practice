import RPi.GPIO as GPIO
import time
pwm=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm,GPIO.OUT)
pwm.start(40)
time.sleep(5)
GPIO.cleanup()