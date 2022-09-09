# Importing neeeded packages
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


while True:
    pass