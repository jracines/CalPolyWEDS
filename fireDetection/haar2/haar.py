from __future__ import print_function
import cv2 as cv
import argparse
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import time
import numpy as np
import sys 
from  datetime import datetime

def draw_rectangles(frame, rectangles):
    line_color = (255,255,0)
    line_type = cv.LINE_4
    for(x, y, w, h) in rectangles:
        top_left = (x,y)
        bottom_right = (x+w, y+h)
        cv.rectangle(frame, top_left, bottom_right, line_color, lineType=line_type)
    return frame


parser = argparse.ArgumentParser(description="")
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
camera_device = args.camera

def main():
    # if(len(sys.argv) < 3):
    #     print('Usage: python3 haar.py <cascade num> <footage num>')
    #     exit()
    
    # cascade_num = sys.argv[1]
    # footage_num = sys.argv[2]

    # # -- 2. Read the video stream (Raspberry Pi Camera)
    cap = cv.VideoCapture(camera_device)
    if not cap.isOpened:
        print('--(!)Error opening video capture')
        exit(0)

    # Reading test raw video of wildfire
    # footage_path = "footage/raw_footage_"+str(footage_num)+".mp4"
    # cap = cv.VideoCapture(footage_path)

    # Error checking
    if not cap.isOpened():
        print("Cannot open capture")
        exit()
    fps = cap.get(cv.CAP_PROP_FPS)

    # Opening cascade classifier
    # cascade_path = 'old_cascades/cascade_'+str(cascade_num)+'/cascade.xml'
    cascade_wildfire = cv.CascadeClassifier('old_cascades/cascade_019/cascade.xml')
    # cascade_wildfire = cv.CascadeClassifier(cascade_path)

    # Resize each image to this width and height
    width = 480
    height = 360
    dim = (width, height)

    loop_time = time()
    while True:
        ret, frame = cap.read()
        if frame is None:
            print('--(!) No captured frame -- Break!')
            break
        # frame = cv.resize(frame, dim, interpolation = cv.INTER_AREA)

        # Testing out cascade classifier
        rectangles = cascade_wildfire.detectMultiScale(frame)
       
        if(len(rectangles) > 0):
            print("Fires detected: ", end='')
            print(len(rectangles))
       
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S") 
        detection_image = draw_rectangles(frame, rectangles)
        # cv.imshow('Cal Poly WEDS Fire Detection', frame)
        cv.imwrite("testphotos/"+current_time+".png",frame)

        key = cv.waitKey(1)
        if key == ord('q'):
            cv.destroyAllWindows()
            break

        # For generating image samples
        # elif key == ord('f'):
        #     print("Saving positive image!")
        #     cv.imwrite('positive/{}.jpg'.format(loop_time), frame)
        # elif key == ord('d'):
        #     print("Saving negative image!")
        #     cv.imwrite('negative/{}.jpg'.format(loop_time), frame)
        # elif key == ord('g'):
        #     print("Saving test image!")
        #     cv.imwrite('tests/{}.jpg'.format(loop_time), frame)

if __name__ == '__main__':
    main()
