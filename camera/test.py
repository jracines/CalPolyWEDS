from picamera import PiCamera
from time import sleep

def main():
    
    camera = PiCamera()

    camera.start_preview()
    # Default resolution: monitor resolution
    # camera.resolution = (2592, 1944)
    camera.resolution = (1920, 1080)
    camera.framerate = 15
    camera.rotation = 180
    sleep(5)
    camera.capture('/home/pi/Desktop/sp/CalPolyWEDS/camera/pyCamTest4.jpg')
    camera.stop_preview()
    # print("hello!")


if __name__ == "__main__":
   main()
