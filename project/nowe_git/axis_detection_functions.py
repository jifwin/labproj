#funkcje powinny zwracac tabele dla osx, osy, prawdopodobonienstwo wynikow w kolejnosci malejacej,
# nastepnei glowna funkcja wybiera z wszystkich kryteriow

import cv2
import numpy as np

pixel_tolerance = 2

def hough(img):

    osx = []
    osy = []

    edges = cv2.Canny(img,50,150,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180,200)

    for item in lines[0,:]:
        if item[1] == np.float32(1.57079637): #pi/2 = 90stopni
            osy.append(item[0])
        if item[1] == 0:
            osx.append(item[0])

    osy.sort(reverse=True) #Y najwyzsze
    osx.sort() #X najnizsze

    osy = map(int,osy)
    osx = map(int,osx)

    return [osx,osy]

def darkest(img):


    #todo: przerobic na numpy array, zeby nie uzywac fora

    osx = []
    osy = []
    osx_values = []
    osy_values = []

    height = img.shape[0]
    width = img.shape[1]


    for [i, item] in enumerate(img[:]): #extract rows
        osy_values.append([i,sum(item)])


    for i in xrange(width):         #extract columns
        osx_values.append([i,sum(img[:,i])])


    osx_values.sort(key=lambda x: x[1])
    osy_values.sort(key=lambda x: x[1])





    for item in osy_values: #extract lines numbers
        osy.append(item[0])

    for item in osx_values: #extract lines numbers
        osx.append(item[0])

    return [osx,osy]



def decide(img,hough,darkest):



    x_hough = hough[0]
    y_hough = hough[1]

    x_darkest = darkest[0]
    y_darkest = darkest[1]

    #dla kazdej wartosci hough sprawdz czy w tolerancji jest darkest i dodac odleglosc od krawedzi (zakladajac wykres 1 cwiartka)

   # for item in x_hough:


def contour(gray):
    ret,thresh = cv2.threshold(gray,127,255,1)
    contours,h = cv2.findContours(thresh,1,cv2.CHAIN_APPROX_SIMPLE) #find counters with aproximation to n-points


    shapes = [] #contains rectangles, then takes maximum (?)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

        if len(approx)==4:
            shapes.append(approx)

    last_shape = shapes[-1]

    #cv2.drawContours(gray,[last_shape],0,(0,0,255),3) # -1 points the whole area

    #cv2.imshow('img',gray)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()


    #todo:rozmknic jak sie robi na numpybez petli

    x_points = []
    y_points = []


    for item in last_shape:
        x_points.append(item[0][0])
        y_points.append(item[0][1])

    #todo: make it to be 2-long only! approx to 15=16 etc


    #find 0-point as minimum/maximum value of x and y
    o_point = [min(x_points), max(y_points)]

    return [o_point,x_points,y_points]