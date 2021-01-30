from picamera import PiCamera
from time import sleep

import sys
import cv2 as cv
import numpy as np

def main():
    
    # camera = PiCamera()

    # camera.start_preview()
    
    # Default resolution: monitor resolution
    # camera.resolution = (2592, 1944)
    # camera.resolution = (1920, 1080)
    # camera.framerate = 15
    # camera.rotation = 180
    # sleep(5)
    # camera.capture('/home/pi/Desktop/sp/CalPolyWEDS/camera/fireDetInput.jpg')
    # camera.stop_preview()

    # img = cv.imread("fireDetInput.jpg", cv.IMREAD_COLOR) 
        
    # cv.imwrite("output.jpg", greyImg)

    face_cascade = cv.CascadeClassifier("opencv/data/haarcascade_frontalface_default.xml")
    eye_cascade = cv.CascadeClassifier("opencv/data/haarcascade_eye.xml")

    img = cv.imread("lena.jpg")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for(x,y,w,h) in faces:
        img = cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # cv.imshow('img', img)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    cv.imwrite("haarout.jpg", img)

if __name__ == "__main__":
   main()
