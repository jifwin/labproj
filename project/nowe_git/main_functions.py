import cv2
import numpy as np
import axis_detection_functions
import labels

def import_image(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print "Image successfully imported"
    return gray

def axis_detection(gray): #todo: czy gorne i boczne granice tez?

    #use? hough = axis_detection_functions.hough(img)
    #use ?darkest = axis_detection_functions.darkest(img)

    #print hough[0]
    #print darkest[0]

    #print hough[1]
    #print darkest[1]

    # detekcja krawedzi pod katem prostym
    # detekcja rogu!!
    #wanze i bedzie dzialac
    #rozwaiaze sporo problemow
    #detekcja punktow w pionie
    #usunac te coernery ktore sa w kupie

    #detekcja ksztaltu L lub prostokat

    #wlasny algorytm do przechodzenia  po pikselach i detekcji linii

    ###AKTUALNE:
   # Contour Detection + Shape Detection
    #todo: detekcja legendy

    [o_point,x_points,y_points] = axis_detection_functions.contour(gray)
    return [o_point,x_points,y_points]

def detect_labels(gray,x_axis,y_axis):

    #crop files according to axis
    [x_crop, y_crop] = labels.crop(gray,x_axis,y_axis)


    [x_labels, y_labels] = labels.ocr()
    #improve: don't use files
    #dopasowanie labeli do skali?

    print x_labels
    print y_labels