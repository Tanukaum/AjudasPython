from PIL import Image
import os
path_img = os.path.dirname(os.path.realpath(__file__)) + '\\Imgs\\Untitled.PNG' 

img = Image.open(path_img)
cor_verde_1 = (8,247,2)
cor_verde_1 = (5,251,1)
cores = []
for cor_rgb in img.getdata():
    if cor_rgb not in cores:
        cores.append(cor_rgb)
#print(cores)

#cores_2 = img.convert('RGB').getcolors(maxcolors=1000)
pixels = img.convert('RGB').load()
print(pixels[2,2])