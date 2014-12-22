import cv2
import numpy as np

img = cv2.imread('smart_wykres.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)

print img.shape # porownac do brzegow


'''
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('houghlines3.jpg',img)
'''


print '---'


pionowe = []
poziome = []

for item in lines[0,:]:
    if item[1] == np.float32(1.57079637):
        poziome.append(item[0])
    if item[1] == 0:
        pionowe.append(item[0])

#podzielic na hertykalne i horyzontalne

poziome.sort()
pionowe.sort()

if 0 in poziome: poziome.remove(0)
if img.shape[0]-1 in poziome: poziome.remove(img.shape[0]-1)
if 0 in pionowe: pionowe.remove(0)
if img.shape[1]-1 in pionowe: pionowe.remove(img.shape[1]-1)

#napisac dokladnie co sie dzieje w programie i sledzic na rysunku!

print 'pionowe:'

print min(pionowe), max(pionowe)
print pionowe

print 'poziome'

print min(poziome), max(poziome)
print poziome


#znalezc najbardziej oddalone oprocz rogow
#konieczna jest korekcja reczna? :((
#wprowadzic inne kryteria, np ciaglosc, odleglosc od legendy, itp
#przeproadzic symulacje roznych parametrow canny?
#polaczyc z kryterium najczarniejszej linii?
#usunac krawedzie obrazu

#wybor krawedzi - czy przecina onne osie, czy lezy odpowiednio blisko i daleko, ewentualnie wybor ktore kontynuowac

print 'wybrane osie'

osx = min(pionowe)
osy = max(poziome)


#sprawdzic punkt przeciecia osi, wyznaczyc punkt 0

zero_point = [osx, osy]
print 'punkt 0: ' + str(zero_point)

cv2.line(img,(osx,0),(osx,osy),(0,0,255),2)
cv2.line(img,(osx,osy),(img.shape[1],osy),(0,0,255),2)
cv2.imwrite('houghlines3.jpg',img)

cv2.imshow('image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#mozliwosc korekcji dolnej krawedzi

#ocr na legende i osie

minimum_line_y = 0
minimum_value = 0

#poziome

for [i, item] in enumerate(gray[:]):
    #print str(i) + ": " + str(item) + "suma: " + str(sum(item)) #czyli to wypisuje w poziomie?
    if minimum_value == 0 or sum(item) < minimum_value:
        minimum_value = sum(item)
        minimum_line_y = i

#print minimum_value #no i to wykrylo poprawna krawedz, teraz zrobic kryterium na 2 metody i wybrac prawidlowa
print minimum_line_y
print osy

if int(minimum_line_y) == int(osy):
    print 'OSY zgadza sie!'
else:
    print 'OSY nie zgadzaja sie!'

