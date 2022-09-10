# Importing neeeded packages
from tkinter import Y
from vpython import *
import numpy as np

# Creating arrows to show axises
arrowLength = 1.5
arrowThickness = .03
rightXarrow = arrow(axis=vector(1,0,0), length=arrowLength, shaftwidth=arrowThickness)
leftXarrow = arrow(axis=vector(-1,0,0), length=arrowLength, shaftwidth=arrowThickness)
topYarrow = arrow(axis=vector(0,1,0), length=arrowLength, shaftwidth=arrowThickness)
bottonYarrow = arrow(axis=vector(0,-1,0), length=arrowLength, shaftwidth=arrowThickness)
frontZarrow = arrow(axis=vector(0,0,1), length=arrowLength, shaftwidth=arrowThickness)
backZarrow = arrow(axis=vector(0,0,-1), length=arrowLength, shaftwidth=arrowThickness)

# ======================================Creating a cubes=================================

#cubies names
'''
centers = {
  Cen1 : white center
  Cen2 : yellow center
  Cen3 : green center
  Cen4 : blue center
  Cen5 : red center
  Cen6 : orange center
}

corners = {
    Cor1 : top front right
    Cor2 : top front left
    Cor3 : top back right
    Cor4 : top back left
    Cor5 : bottom front right 
    Cor6 : bottom front left 
    Cor7 : bottom back right 
    Cor8 : bottom back left
}

edges = {
  Edg1 : top front
  Edg2 : top right
  Edg3 : top back
  Edg4 : top left
  Edg5 : middle front right
  Edg6 : middle front left
  Edg7 : middle back right
  Edg8 : middle back left
  Edg9 : bottom front
  Edg10 : bottom right
  Edg11 : bottom back
  Edge12 : bottom left
}
'''

cubePyramids = [
    pyramid(size=vector(0.5,1,1), pos=vector(0,0.5,0), axis=vector(0,-1,0), color=color.white),
    pyramid(size=vector(0.5,1,1), pos=vector(0,-0.5,0), axis=vector(0,1,0), color=color.yellow),
    pyramid(size=vector(0.5,1,1), pos=vector(0.5,0,0), axis=vector(-1,0,0), color=color.red),
    pyramid(size=vector(0.5,1,1), pos=vector(-0.5,0,0), axis=vector(1,0,0), color=color.orange),
    pyramid(size=vector(0.5,1,1), pos=vector(0,0,0.5), axis=vector(0,0,-1), color=color.green),
    pyramid(size=vector(0.5,1,1), pos=vector(0,0,-0.5), axis=vector(0,0,1), color=color.blue)
]


while True:
    pass