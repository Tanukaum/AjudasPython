from PIL import Image
import os
path_img = os.path.dirname(os.path.realpath(__file__)) + '\\Imgs\\imgcolorida.PNG' 

img = Image.open(path_img)

cores = []
for cor_rgb in img.getdata():
    if cor_rgb not in cores:
        cores.append(cor_rgb)
print(cores)
