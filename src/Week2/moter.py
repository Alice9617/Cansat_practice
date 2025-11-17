import RPi.GPIO as GPIO

motor_Left= 18
motor_Right= 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_Left and motor_Right, GPIO.OUT)

pwm=GPIO.PWM(motor_Left and motor_Right, 50)
pwm.start(0)

def move(duty:int,dir:str):
    All=motor_Left,motor_Right
    if dir == "forward":
        All.start(40)
    elif dir == "Right":
        motor_Right.start(0)
        motor_Left.start(40)
    elif dir == "Left":
        motor_Left.start(0)
        motor_Right.start(40)
    else:
        All.start(0)

if __name__=="__main__":
    duty,dir = input("duty,dir = ").split(",")
    move(duty,dir)
