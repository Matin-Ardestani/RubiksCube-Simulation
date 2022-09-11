# Importing neeeded packages
from calendar import c
from vpython import *
import numpy as np

# Creating arrows to show axises
arrowLength = 1.52
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
  CenW : white center
  CenY : yellow center
  CenG : green center
  CenB : blue center
  CenR : red center
  CenO : orange center
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

# Global variables
cubySize = vector(1,1,1)
dis = .01 # distant size

# Creatin cubes using 6 pyramids with 6 different colors
cubePyramids = [
    pyramid(size=vector(0.5,1,1), pos=vector(0,0.5,0), axis=vector(0,-1,0), color=color.white),
    pyramid(size=vector(0.5,1,1), pos=vector(0,-0.5,0), axis=vector(0,1,0), color=color.yellow),
    pyramid(size=vector(0.5,1,1), pos=vector(0.5,0,0), axis=vector(-1,0,0), color=color.red),
    pyramid(size=vector(0.5,1,1), pos=vector(-0.5,0,0), axis=vector(1,0,0), color=color.orange),
    pyramid(size=vector(0.5,1,1), pos=vector(0,0,0.5), axis=vector(0,0,-1), color=color.green),
    pyramid(size=vector(0.5,1,1), pos=vector(0,0,-0.5), axis=vector(0,0,1), color=color.blue)
]

# Right side
CenR = compound(cubePyramids)
CenR.size , CenR.pos = cubySize, vector(1+dis,0,0)

Cor1 = compound(cubePyramids)
Cor1.size, Cor1.pos = cubySize, vector(1+dis,1+dis,1+dis)
Cor3 = compound(cubePyramids)
Cor3.size, Cor3.pos = cubySize, vector(1+dis,1+dis,-1-dis)
Cor5 = compound(cubePyramids)
Cor5.size, Cor5.pos = cubySize, vector(1+dis,-1-dis,1+dis)
Cor7 = compound(cubePyramids)
Cor7.size, Cor7.pos = cubySize, vector(1+dis,-1-dis,-1-dis)

Edg2 = compound(cubePyramids)
Edg2.size, Edg2.pos = cubySize, vector(1+dis,1+dis,0)
Edg5 = compound(cubePyramids)
Edg5.size, Edg5.pos = cubySize, vector(1+dis,0,1+dis)
Edg7 = compound(cubePyramids)
Edg7.size, Edg7.pos = cubySize, vector(1+dis,0,-1-dis)
Edg10 = compound(cubePyramids)
Edg10.size, Edg10.pos = cubySize, vector(1+dis,-1-dis,0)



# Positions names & dictionary
Positions = {
    'C1' : Cor1,
    'C3' : Cor3,
    'C5' : Cor5,
    'C7' : Cor7
}


# ===================================Moves=====================================================
# Convert degree to radian
def convert_to_radius(degree):
    return degree * (np.pi / 180)

def R_move(x):
    CorBallancePositions = list(np.linspace(1+dis, np.sqrt(2), 45)) + list(np.linspace(np.sqrt(2), 1+dis, 45)) # for better movement we use 2 steps
    CorChangePositions = np.linspace(1+dis, -1-dis, 90)
    EdgIncPositions = list(np.linspace(0, .5, 30)) + list(np.linspace(.5, 1+dis, 60)) # for better movement we use 2 steps with 2 different sizes
    EdgDecPositions = list(np.linspace(1+dis, .5, 60)) + list(np.linspace(.5, 0, 30)) # for better movement we use 2 steps with 2 different sizes
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenR.rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))

        # Corners moves
        Positions['C1'].pos = vector(1+dis, CorBallancePos, CorChangePos)
        Positions['C1'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['C3'].pos = vector(1+dis, CorChangePos, -CorBallancePos)
        Positions['C3'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['C5'].pos = vector(1+dis, -CorChangePos, CorBallancePos)
        Positions['C5'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['C7'].pos = vector(1+dis, -CorBallancePos, -CorChangePos)
        Positions['C7'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))

        # Edge moves
        Edg2.pos = vector(1+dis, EdgDecPos, -EdgIncPos)
        Edg2.rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Edg5.pos = vector(1+dis, EdgIncPos, EdgDecPos)
        Edg5.rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Edg7.pos = vector(1+dis, -EdgIncPos, -EdgDecPos)
        Edg7.rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Edg10.pos = vector(1+dis, -EdgDecPos, EdgIncPos)
        Edg10.rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
    
    # Change cubies positions
    Positions['C1'] = Cor5
    Positions['C3'] = Cor1
    Positions['C5'] = Cor7
    Positions['C7'] = Cor3

def Rpr_move(x):
    CorBallancePositions = list(np.linspace(1+dis, np.sqrt(2), 45)) + list(np.linspace(np.sqrt(2), 1+dis, 45)) # for better movement we use 2 steps
    CorChangePositions = np.linspace(1+dis, -1-dis, 90)
    EdgIncPositions = list(np.linspace(0, .5, 30)) + list(np.linspace(.5, 1+dis, 60)) # for better movement we use 2 steps with 2 different sizes
    EdgDecPositions = list(np.linspace(1+dis, .5, 60)) + list(np.linspace(.5, 0, 30)) # for better movement we use 2 steps with 2 different sizes
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenR.rotate(axis=vector(1,0,0), angle=convert_to_radius(1))

        # Corners moves
        Positions['C1'].pos = vector(1+dis, CorChangePos, CorBallancePos)
        Positions['C1'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['C3'].pos = vector(1+dis, CorBallancePos, -CorChangePos)
        Positions['C3'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['C5'].pos = vector(1+dis, -CorBallancePos, CorChangePos)
        Positions['C5'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['C7'].pos = vector(1+dis, -CorChangePos, -CorBallancePos)
        Positions['C7'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))

        # # Edge moves
        Edg2.pos = vector(1+dis, EdgDecPos, EdgIncPos)
        Edg2.rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Edg5.pos = vector(1+dis, -EdgIncPos, EdgDecPos)
        Edg5.rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Edg7.pos = vector(1+dis, EdgIncPos, -EdgDecPos)
        Edg7.rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Edg10.pos = vector(1+dis, -EdgDecPos, -EdgIncPos)
        Edg10.rotate(axis=vector(1,0,0), angle=convert_to_radius(1))

    # Change cubies positions
    Positions['C1'] = Cor3
    Positions['C3'] = Cor7
    Positions['C5'] = Cor1
    Positions['C7'] = Cor5
        
       

# Button widgets
button(bind=R_move, text="  R  ", background=color.red, color=color.black)
scene.append_to_caption('\t')
button(bind=Rpr_move, text="  R'  ", background=color.red, color=color.black)


while True:
    pass