#This file contains main activity of chart converter
#usage:
#python2 main.py filename

import sys
import main_functions


if(len(sys.argv) < 2): #if filename argument specified
    print "Filename not specified!"
    sys.exit(1)

filename = sys.argv[1]

#Importing image in gray
img = main_functions.import_image(filename)

#Axis detection

if(len(sys.argv) > 3): #if axes specified as argument
    o_point = [sys.argv[2], sys.argv[3]]
    sys.exit(2)
else:
    [o_point,x_points,y_points] = main_functions.axis_detection(img)


print [o_point,x_points,y_points]
# na tej podstawie dopasowac max do labeli

sys.exit(2) #temporary

#Zero point detection


#if (len(axes) == 2):
#    zero = axes



#Legend Detection

#OCR Label detection

main_functions.detect_labels(img,o_point[0],o_point[1])


#Points detection

sys.exit(0) #success