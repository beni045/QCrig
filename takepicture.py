import numpy as np
import cv2
from random import randrange
import picamera


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite('/home/pi/Desktop/pictures/opencv/image_' + str(randrange(1000000)) + '.jpg', frame)
    cap.release()
    cv2.destroyAllWindows()
    
    camera = picamera.PiCamera()
    camera.resolution = (3280,2464)
    camera.capture('/home/pi/Desktop/pictures/picamera/image_' + str(randrange(1000000)) + '.jpg')


 