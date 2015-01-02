__author__ = 'grzegorz'
import cv2
from pytesser import *
import numpy as np


def crop(gray,x_axis,y_axis):
    x_cropped_img = gray[y_axis:,:]
    y_cropped_img = gray[:,:x_axis]

    x_cropped_img = cv2.resize(x_cropped_img, (0,0), fx=5, fy=5)
    y_cropped_img = cv2.resize(y_cropped_img, (0,0), fx=5, fy=5)

    cv2.imwrite('x_cropped_img.png',x_cropped_img)
    cv2.imwrite('y_cropped_img.png',y_cropped_img)
    #cv2.imshow("x_cropped",x_cropped_img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    #cv2.imshow("x_cropped",y_cropped_img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    return [x_cropped_img,y_cropped_img]

def ocr(): #input cropped img

    x_labels_str = image_file_to_string('x_cropped_img.png')
    y_labels_str = image_file_to_string('y_cropped_img.png')
    #todo: najpierw objac w bounding rectangle?
    #rozpoznawac osobno kazda liczbe? (omija niektore)..

    #todo: improve: psm for 7 too?
    #todo: don't use files?

    x_labels = x_labels_str.split(" ")
    y_labels = y_labels_str.split("\n")
    #todo: delete "\n", and " "

    while '' in x_labels:
        x_labels.remove('')

    while '' in y_labels:
        y_labels.remove('')

    #replace O-letter with 0-digit
    x_labels = [label.replace("O","0") for label in x_labels]
    x_labels = [label.replace("\n","") for label in x_labels]
    x_labels = [label.replace(" ","") for label in x_labels]


    y_labels = [label.replace("O","0") for label in y_labels]
    y_labels = [label.replace("o","0") for label in y_labels]
    y_labels = [label.replace("\n","") for label in y_labels]
    y_labels = [label.replace(" ","") for label in y_labels]

    #improve performence?
    #remove extra chars, starting with minus,
    #do some regular expressions
    #obcinac do ostatniego poprawnego znaku

    x_labels = [float(i) for i in x_labels]
    y_labels = [float(i) for i in y_labels]



    return [x_labels, y_labels]

