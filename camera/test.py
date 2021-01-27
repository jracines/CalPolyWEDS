from picamera import PiCamera
from time import sleep

import sys
import cv2 as cv
import numpy as np

def main():
    
    camera = PiCamera()

    camera.start_preview()
    # Default resolution: monitor resolution
    # camera.resolution = (2592, 1944)
    # camera.resolution = (1920, 1080)
    camera.framerate = 15
    camera.rotation = 180
    sleep(5)
    camera.capture('/home/pi/Desktop/sp/CalPolyWEDS/camera/fireDetInput.jpg')
    camera.stop_preview()

    img = cv.imread("fireDetInput.jpg", cv.IMREAD_COLOR) 
    greyImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite("output.jpg", greyImg)


if __name__ == "__main__":
   main()
