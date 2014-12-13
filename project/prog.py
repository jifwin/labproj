from PIL import Image
im = Image.open("wykres.jpg")
pix = im.load()
print im.size
print pix[0,0]
