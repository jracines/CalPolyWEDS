from picamera import PiCamera
from time import sleep

def main():
    
    camera = PiCamera()

    camera.start_preview()
    camera.rotation = 180
    sleep(5)
    camera.capture('/home/pi/Desktop/sp/CalPolyWEDS/camera/pyCamTest.jpg')
    camera.stop_preview()
    # print("hello!")


if __name__ == "__main__":
   main()
