from picamera import Picamera2
from datetime import datetime

def capture(height,width,cnt):
    picam2=Picamera2()

    config=picam2.create_still_configuration(main={"size":(width,height)})
    picam2.configure(config)
    
    picam2.start()
    
    filename=""

    picam2.capture_file(filename)

    picam2.close()


