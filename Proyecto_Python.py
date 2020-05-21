# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:59:42 2020

@author: Cesar Ramos
"""
# Previously Pillow library is required
from PIL import Image
import os
sharp = Image.open('img3.jpg')

#To show the image
sharp.show()
#To se the size of the figure (width, height)
# (1002, 1002)
print(sharp.size)
# Show the name and the extension for the figure
print(sharp.filename)
# More detail for the figure
print(sharp.format_description)

# Cropping Images
# Cortamos la imagen en 4
# Parte 1
cutit1 = sharp.crop((0, 0, 500, 500))
# Parte 4
cutit2 = sharp.crop((500, 500, 1000, 1000))
# Parte 3
cutit3 = sharp.crop((0, 500, 500, 1000))
# Parte 2
cutit4 = sharp.crop((500, 0, 1000, 500))

cutit3.show()
path = "saveit"

# Guarda la imagen en la ruta con el nombre cutit3.jpg
cutit1.save('D:\github_cesar\ProyFin\saveit/cutit1.jpg')
cutit2.save('D:\github_cesar\ProyFin\saveit/cutit2.jpg')
cutit3.save('D:\github_cesar\ProyFin\saveit/cutit3.jpg')
cutit4.save('D:\github_cesar\ProyFin\saveit/cutit4.jpg')

print(cutit1.size)
print(cutit2.size)
print(cutit3.size)
print(cutit4.size)


pencils = Image.open('pencils.jpg')
pencils.show()
pencils.size
pencils.filename
# Bottom pencils
x = 0
y = 0
w = 398/1.2
h = 600/5
pencils.crop((x, y, w, h))

# Rezise images
pencils.size
pencils_r = pencils.resize((400, 600))
pencils_r.size

# Rotate images
pencils.rotate(180)

########################################
########################################
#########  Color Transparency ##########
########################################
########################################

# RGBA Red Green Blue Alpha

red = Image.open('red_color.jpg')
red = red.resize((400,400))
red.show()
blue = Image.open('blue_color.jpg')
blue = blue.resize((400,400))
blue.show()

# Transparecnia de 0 a 100 enteros
blue.putalpha(99)
blue

red.putalpha(255)
red
