import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
def move(duty:int,dir:str) -> None:
    if dir=="forward":
        """
        前進
        """
    elif dir=="right":
        """
        右折
        """
    elif dir =="left":
        """
        左折
        """
    else:
        """
        停止
        """
    if __name__=="__main__":
        duty,dir=input("duty,dir=").split(",")
        move(duty,dir)