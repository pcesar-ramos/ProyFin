# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:59:42 2020

@author: Usuario
"""
# Previously Pillow library is required
from PIL import Image

mac = Image.open('img3.jpg')

#To show the image
mac.show()
#To se the size of the figure (width, height)
# (1002, 1002)
print(mac.size)
# Show the name and the extension for the figure
print(mac.filename)
# More detail for the figure
print(mac.format_description)

# Cropping Images
# Cortamos la imagen en 4
# Parte 1
cutit1 = mac.crop((0, 0, 500, 500))
# Parte 4
cutit2 = mac.crop((500, 500, 1000, 1000))
# Parte 3
cutit3 = mac.crop((0, 500, 500, 1000))
# Parte 2
cutit4 = mac.crop((500, 0, 1000, 500))

cutit3.show()

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