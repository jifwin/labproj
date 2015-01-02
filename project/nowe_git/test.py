import cv2
import numpy as np

img = cv2.imread('wykresy/5.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)


minLineLength = 10000#img.shape[0]*0.8
maxLineGap = 300


#lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
lines = cv2.HoughLinesP(edges,1,np.pi/180,800)



for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

print lines

#zmmieniaj te parametry az znalezione zostana 4 rozne wspolrzedne


cv2.imwrite('houghlines5.jpg',img)