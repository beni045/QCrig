from configparser import ConfigParser
import cv2
from sole_size import find_sides
import numpy as np


class Tester():
    def __init__(self):
        parser = ConfigParser()
        parser.read('config.ini')
        self.sole_size_params = parser._sections['sole_size_params']
        self.sole_data = {}
        self.cropped = None

    def calc_size(self, img, crop):
        self.cropped, top, left, right = find_sides(
                img, 
                float(self.sole_size_params['color_thresh']), 
                int(self.sole_size_params['calib_slice_range']), 
                float(self.sole_size_params['calib_x']), 
                float(self.sole_size_params['calib_y']),
                float(self.sole_size_params['crop_y_top']), 
                float(self.sole_size_params['crop_y_bottom']), 
                float(self.sole_size_params['crop_center']),
                crop)

        return top, left, right

        
            
if __name__ == '__main__':
    img = cv2.imread("/home/pi/Desktop/pictures/opencv/image_689391.jpg")
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    which_test = 1

    if which_test == 0:
        y1 = 110  # ALIGN WITH 30CM
        y2 = 500  # ALIGN WITH 10CM

        size_conv_factor = 200 / (y2 - y1) 
        print('size conv factor: ', size_conv_factor)

        offset = 300 - ((img.shape[0] - y1) * size_conv_factor)
        print('offset: ', offset)

        cv2.line(img, (0, y1), (img.shape[1], y1), (255,0,0), 2)
        cv2.line(img, (0, y2), (img.shape[1], y2), (255,0,0), 2)
        cv2.imshow('pic', img)
        k = cv2.waitKey(0) # 0==wait forever



    else:
        testy = Tester()
        top, left, right = testy.calc_size(img, True)

        cv2.imshow('pic', img)
        #k = cv2.waitKey(0) # 0==wait forever

        cv2.line(img, (0, top), (img.shape[1], top), (255,0,0), 2)
        cv2.line(img, (left, 0), (left, img.shape[0]), (255,0,0), 2)
        cv2.line(img, (right, 0), (right, img.shape[0]), (255,0,0), 2)

        calib_line = round(float(testy.sole_size_params['side_test_line']) * img.shape[1])

        cv2.line(img, (calib_line, 0), (calib_line, img.shape[0]), (255,0,0), 2)


        print('left, right:', calib_line - left, right - calib_line)

        cv2.imshow('pic', testy.cropped)
        #k = cv2.waitKey(0) # 0==wait forever

        cv2.imshow('pic', img)
        k = cv2.waitKey(0) # 0==wait forever

 


    




