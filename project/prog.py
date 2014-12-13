from PIL import Image
im = Image.open("wykres.bmp")
pix = im.load()
print im.size


