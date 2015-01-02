import cv2
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxint)

filename = sys.argv[1]
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,31,0.04)



#for [i, item] in enumerate(dst): # leci po y
#    print str(i) + ":" + str(item)


#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)


dst = dst/dst.max()
print dst.max()

corners = []


#for [i, item1] in enumerate(dst):#y
#    for [j, item2] in enumerate(dst[i]):#x
#        if item2 != 0:
#            if i > 35 and i < 75 and j < 400 and j > 350:
#                print str(i) + ":"  + str(j) + ": " + str(item2)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

for i in xrange(dst.shape[0]):
    for j in xrange(dst.shape[1]):

        #count how many points around are not zero

        count = 0

        #for

        #print dst[i,j]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


# konwersja tej macierzy do macierzy typu x, y corner