# Importing neeeded packages
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

# Creating cubies using 6 pyramids with 6 different colors
cubePyramids = [
    pyramid(size=vector(0.5,1,1), pos=vector(0,0.5,0), axis=vector(0,-1,0), color=color.white),
    pyramid(size=vector(0.5,1,1), pos=vector(0,-0.5,0), axis=vector(0,1,0), color=color.yellow),
    pyramid(size=vector(0.5,1,1), pos=vector(0.5,0,0), axis=vector(-1,0,0), color=color.red),
    pyramid(size=vector(0.5,1,1), pos=vector(-0.5,0,0), axis=vector(1,0,0), color=color.orange),
    pyramid(size=vector(0.5,1,1), pos=vector(0,0,0.5), axis=vector(0,0,-1), color=color.green),
    pyramid(size=vector(0.5,1,1), pos=vector(0,0,-0.5), axis=vector(0,0,1), color=color.blue)
]

# Creating Center cubies
CenR = compound(cubePyramids)
CenR.size , CenR.pos = cubySize, vector(1+dis,0,0)
CenW = compound(cubePyramids)
CenW.size, CenW.pos = cubySize, vector(0,1+dis,0)
CenB = compound(cubePyramids)
CenB.size, CenB.pos = cubySize, vector(0,0,-1-dis)
CenO = compound(cubePyramids)
CenO.size, CenO.pos = cubySize, vector(-1-dis,0,0)
CenY = compound(cubePyramids)
CenY.size, CenY.pos = cubySize, vector(0,-1-dis,0)
CenG = compound(cubePyramids)
CenG.size, CenG.pos = cubySize, vector(0,0,1+dis)

# Creating Corner cubies
Cor1 = compound(cubePyramids)
Cor1.size, Cor1.pos = cubySize, vector(1+dis,1+dis,1+dis)
Cor3 = compound(cubePyramids)
Cor3.size, Cor3.pos = cubySize, vector(1+dis,1+dis,-1-dis)
Cor5 = compound(cubePyramids)
Cor5.size, Cor5.pos = cubySize, vector(1+dis,-1-dis,1+dis)
Cor7 = compound(cubePyramids)
Cor7.size, Cor7.pos = cubySize, vector(1+dis,-1-dis,-1-dis)
Cor8 = compound(cubePyramids)
Cor8.size, Cor8.pos = cubySize, vector(-1-dis,-1-dis,-1-dis)
Cor2 = compound(cubePyramids)
Cor2.size, Cor2.pos = cubySize, vector(-1-dis, 1+dis, 1+dis)
Cor4 = compound(cubePyramids)
Cor4.size, Cor4.pos = cubySize, vector(-1-dis, 1+dis, -1-dis)
Cor6 = compound(cubePyramids)
Cor6.size, Cor6.pos = cubySize, vector(-1-dis, -1-dis, 1+dis)

# Creating Edge cubies
Edg2 = compound(cubePyramids)
Edg2.size, Edg2.pos = cubySize, vector(1+dis,1+dis,0)
Edg5 = compound(cubePyramids)
Edg5.size, Edg5.pos = cubySize, vector(1+dis,0,1+dis)
Edg7 = compound(cubePyramids)
Edg7.size, Edg7.pos = cubySize, vector(1+dis,0,-1-dis)
Edg10 = compound(cubePyramids)
Edg10.size, Edg10.pos = cubySize, vector(1+dis,-1-dis,0)
Edg1 = compound(cubePyramids)
Edg1.size, Edg1.pos = cubySize, vector(0, 1+dis, 1+dis)
Edg3 = compound(cubePyramids)
Edg3.size, Edg3.pos = cubySize, vector(0, 1+dis, -1-dis)
Edg4 = compound(cubePyramids)
Edg4.size, Edg4.pos = cubySize, vector(-1-dis, 1+dis, 0)
Edg8 = compound(cubePyramids)
Edg8.size, Edg8.pos = cubySize, vector(-1-dis, 0, -1-dis)
Edg11 = compound(cubePyramids)
Edg11.size, Edg11.pos = cubySize, vector(0, -1-dis, -1-dis)
Edg6 = compound(cubePyramids)
Edg6.size, Edg6.pos = cubySize, vector(-1-dis, 0, 1+dis)
Edg12 = compound(cubePyramids)
Edg12.size, Edg12.pos = cubySize, vector(-1-dis, -1-dis, 0)
Edg9 = compound(cubePyramids)
Edg9.size, Edg9.pos = cubySize, vector(0, -1-dis, 1+dis)


# Positions names & dictionary
Positions = {
    'C1' : Cor1,
    'C3' : Cor3,
    'C5' : Cor5,
    'C7' : Cor7,
    'C2' : Cor2,
    'C4' : Cor4,
    'C8' : Cor8,
    'C6' : Cor6,

    'E2' : Edg2,
    'E5' : Edg5,
    'E7' : Edg7,
    'E10' : Edg10,
    'E1' : Edg1,
    'E3' : Edg3,
    'E4' : Edg4,
    'E8' : Edg8,
    'E11' : Edg11,
    'E6' : Edg6,
    'E12' : Edg12,
    'E9' : Edg9
}


# ===================================Moves=====================================================
# Convert degree to radian
def convert_to_radius(degree):
    return degree * (np.pi / 180)

# Changing axis positions ( we use them in loops for moving sides )
CorBallancePositions = list(np.linspace(1+dis, np.sqrt(2), 45)) + list(np.linspace(np.sqrt(2), 1+dis, 45)) # for better movement we use 2 steps
CorChangePositions = np.linspace(1+dis, -1-dis, 90)
EdgIncPositions = list(np.linspace(0, .5, 30)) + list(np.linspace(.5, 1+dis, 60)) # for better movement we use 2 steps with 2 different sizes (Edge Increase Position)
EdgDecPositions = list(np.linspace(1+dis, .5, 60)) + list(np.linspace(.5, 0, 30)) # for better movement we use 2 steps with 2 different sizes (Edge Decrease Position)

# R move
def r_move(turn):
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
        Positions['E2'].pos = vector(1+dis, EdgDecPos, -EdgIncPos)
        Positions['E2'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['E5'].pos = vector(1+dis, EdgIncPos, EdgDecPos)
        Positions['E5'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['E7'].pos = vector(1+dis, -EdgIncPos, -EdgDecPos)
        Positions['E7'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['E10'].pos = vector(1+dis, -EdgDecPos, EdgIncPos)
        Positions['E10'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
    
    # Change cubies positions
    Positions['C1'], Positions['C3'], Positions['C5'], Positions['C7'] = Positions['C5'], Positions['C1'], Positions['C7'], Positions['C3']
    Positions['E2'], Positions['E5'], Positions['E7'], Positions['E10'] = Positions['E5'], Positions['E10'], Positions['E2'], Positions['E7']
    
    if turn == 2:
        R_move(1)

# R' move
def rpr_move(x):
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
        Positions['E2'].pos = vector(1+dis, EdgDecPos, EdgIncPos)
        Positions['E2'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['E5'].pos = vector(1+dis, -EdgIncPos, EdgDecPos)
        Positions['E5'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['E7'].pos = vector(1+dis, EdgIncPos, -EdgDecPos)
        Positions['E7'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['E10'].pos = vector(1+dis, -EdgDecPos, -EdgIncPos)
        Positions['E10'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))

    # Change cubies positions
    Positions['C1'], Positions['C3'], Positions['C5'], Positions['C7'] = Positions['C3'], Positions['C7'], Positions['C1'], Positions['C5']
    Positions['E2'], Positions['E5'], Positions['E7'], Positions['E10'] = Positions['E7'], Positions['E2'], Positions['E10'], Positions['E5']

# U move
def u_move(turn):
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenW.rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))

        # Corners moves
        Positions['C1'].pos = vector(CorChangePos, 1+dis, CorBallancePos)
        Positions['C1'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['C3'].pos = vector(CorBallancePos, 1+dis, -CorChangePos)
        Positions['C3'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['C2'].pos = vector(-CorBallancePos, 1+dis, CorChangePos)
        Positions['C2'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['C4'].pos = vector(-CorChangePos, 1+dis, -CorBallancePos)
        Positions['C4'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))

        # Edge moves
        Positions['E2'].pos = vector(EdgDecPos, 1+dis, EdgIncPos)
        Positions['E2'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['E1'].pos = vector(-EdgIncPos, 1+dis, EdgDecPos)
        Positions['E1'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['E3'].pos = vector(EdgIncPos, 1+dis, -EdgDecPos)
        Positions['E3'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['E4'].pos = vector(-EdgDecPos, 1+dis, -EdgIncPos)
        Positions['E4'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))

    # Change cubies positions
    Positions['C1'], Positions['C2'], Positions['C3'], Positions['C4'] = Positions['C3'], Positions['C1'], Positions['C4'], Positions['C2']
    Positions['E1'], Positions['E2'], Positions['E3'], Positions['E4'] = Positions['E2'], Positions['E3'], Positions['E4'], Positions['E1']
    
    # Recalling the Function for moves with a 2
    if turn == 2:
        U_move(1)

# U' move
def upr_move(x):
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenW.rotate(axis=vector(0,1,0), angle=convert_to_radius(1))

        # Corners moves
        Positions['C1'].pos = vector(CorBallancePos, 1+dis, CorChangePos)
        Positions['C1'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['C3'].pos = vector(CorChangePos, 1+dis, -CorBallancePos)
        Positions['C3'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['C2'].pos = vector(-CorChangePos, 1+dis, CorBallancePos)
        Positions['C2'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['C4'].pos = vector(-CorBallancePos, 1+dis, -CorChangePos)
        Positions['C4'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))

        # Edge moves
        Positions['E2'].pos = vector(EdgDecPos, 1+dis, -EdgIncPos)
        Positions['E2'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['E1'].pos = vector(EdgIncPos, 1+dis, EdgDecPos)
        Positions['E1'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['E3'].pos = vector(-EdgIncPos, 1+dis, -EdgDecPos)
        Positions['E3'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['E4'].pos = vector(-EdgDecPos, 1+dis, EdgIncPos)
        Positions['E4'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))

    # Change cubies positions
    Positions['C1'], Positions['C2'], Positions['C3'], Positions['C4'] = Positions['C2'], Positions['C4'], Positions['C1'], Positions['C3']
    Positions['E1'], Positions['E2'], Positions['E3'], Positions['E4'] = Positions['E4'], Positions['E1'], Positions['E2'], Positions['E3']

# B move
def b_move(turn):
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenB.rotate(axis=vector(0,0,1), angle=convert_to_radius(1))

        # Corners moves
        Positions['C3'].pos = vector(CorChangePos, CorBallancePos, -1-dis)
        Positions['C3'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['C4'].pos = vector(-CorBallancePos, CorChangePos, -1-dis)
        Positions['C4'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['C7'].pos = vector(CorBallancePos, -CorChangePos, -1-dis)
        Positions['C7'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['C8'].pos = vector(-CorChangePos, -CorBallancePos, -1-dis)
        Positions['C8'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))

        # Edge moves
        Positions['E3'].pos = vector(-EdgIncPos, EdgDecPos, -1-dis)
        Positions['E3'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['E7'].pos = vector(EdgDecPos, EdgIncPos, -1-dis)
        Positions['E7'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['E8'].pos = vector(-EdgDecPos, -EdgIncPos, -1-dis)
        Positions['E8'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['E11'].pos = vector(EdgIncPos, -EdgDecPos, -1-dis)
        Positions['E11'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
    
    # Change cubies positions
    Positions['C3'], Positions['C4'], Positions['C7'], Positions['C8'] = Positions['C7'], Positions['C3'], Positions['C8'], Positions['C4']
    Positions['E3'], Positions['E7'], Positions['E8'], Positions['E11'] = Positions['E7'], Positions['E11'], Positions['E3'], Positions['E8']
    
    # Recalling the Function for moves with a 2
    if turn == 2:
        B_move(1)

# B' move
def bpr_move(x):
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenB.rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))

        # Corners moves
        Positions['C3'].pos = vector(CorBallancePos, CorChangePos, -1-dis)
        Positions['C3'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['C4'].pos = vector(-CorChangePos, CorBallancePos, -1-dis)
        Positions['C4'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['C7'].pos = vector(CorChangePos, -CorBallancePos, -1-dis)
        Positions['C7'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['C8'].pos = vector(-CorBallancePos, -CorChangePos, -1-dis)
        Positions['C8'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))

        # Edge moves
        Positions['E3'].pos = vector(EdgIncPos, EdgDecPos, -1-dis)
        Positions['E3'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['E7'].pos = vector(EdgDecPos, -EdgIncPos, -1-dis)
        Positions['E7'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['E8'].pos = vector(-EdgDecPos, EdgIncPos, -1-dis)
        Positions['E8'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['E11'].pos = vector(-EdgIncPos, -EdgDecPos, -1-dis)
        Positions['E11'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
    
    # Change cubies positions
    Positions['C3'], Positions['C4'], Positions['C7'], Positions['C8'] = Positions['C4'], Positions['C8'], Positions['C3'], Positions['C7']
    Positions['E3'], Positions['E7'], Positions['E8'], Positions['E11'] = Positions['E8'], Positions['E3'], Positions['E11'], Positions['E7']

# L move
def l_move(turn):
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenO.rotate(axis=vector(1,0,0), angle=convert_to_radius(1))

        # Corners moves
        Positions['C2'].pos = vector(-1-dis, CorChangePos, CorBallancePos)
        Positions['C2'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['C4'].pos = vector(-1-dis, CorBallancePos, -CorChangePos)
        Positions['C4'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['C6'].pos = vector(-1-dis, -CorBallancePos, CorChangePos)
        Positions['C6'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['C8'].pos = vector(-1-dis, -CorChangePos, -CorBallancePos)
        Positions['C8'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))

        # Edge moves
        Positions['E4'].pos = vector(-1-dis, EdgDecPos, EdgIncPos)
        Positions['E4'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['E6'].pos = vector(-1-dis, -EdgIncPos, EdgDecPos)
        Positions['E6'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['E8'].pos = vector(-1-dis, EdgIncPos, -EdgDecPos)
        Positions['E8'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
        Positions['E12'].pos = vector(-1-dis, -EdgDecPos, -EdgIncPos)
        Positions['E12'].rotate(axis=vector(1,0,0), angle=convert_to_radius(1))
    
    # Change cubies positions
    Positions['C2'], Positions['C4'], Positions['C6'], Positions['C8'] = Positions['C4'], Positions['C8'], Positions['C2'], Positions['C6']
    Positions['E4'], Positions['E6'], Positions['E8'], Positions['E12'] = Positions['E8'], Positions['E4'], Positions['E12'], Positions['E6']
    
    # Recalling the Function for moves with a 2
    if turn == 2:
        L_move(1)

# L' move
def lpr_move(x):
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenO.rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))

        # Corners moves
        Positions['C2'].pos = vector(-1-dis, CorBallancePos, CorChangePos)
        Positions['C2'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['C4'].pos = vector(-1-dis, CorChangePos, -CorBallancePos)
        Positions['C4'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['C6'].pos = vector(-1-dis, -CorChangePos, CorBallancePos)
        Positions['C6'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['C8'].pos = vector(-1-dis, -CorBallancePos, -CorChangePos)
        Positions['C8'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))

        # Edge moves
        Positions['E4'].pos = vector(-1-dis, EdgDecPos, -EdgIncPos)
        Positions['E4'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['E6'].pos = vector(-1-dis, EdgIncPos, EdgDecPos)
        Positions['E6'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['E8'].pos = vector(-1-dis, -EdgIncPos, -EdgDecPos)
        Positions['E8'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
        Positions['E12'].pos = vector(-1-dis, -EdgDecPos, EdgIncPos)
        Positions['E12'].rotate(axis=vector(1,0,0), angle=convert_to_radius(-1))
    
    # Change cubies positions
    Positions['C2'], Positions['C4'], Positions['C6'], Positions['C8'] = Positions['C6'], Positions['C2'], Positions['C8'], Positions['C4']
    Positions['E4'], Positions['E6'], Positions['E8'], Positions['E12'] = Positions['E6'], Positions['E12'], Positions['E4'], Positions['E8']

# D move
def d_move(turn):
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenY.rotate(axis=vector(0,1,0), angle=convert_to_radius(1))

        # Corners moves
        Positions['C5'].pos = vector(CorBallancePos, -1-dis, CorChangePos)
        Positions['C5'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['C7'].pos = vector(CorChangePos, -1-dis, -CorBallancePos)
        Positions['C7'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['C6'].pos = vector(-CorChangePos, -1-dis, CorBallancePos)
        Positions['C6'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['C8'].pos = vector(-CorBallancePos, -1-dis, -CorChangePos)
        Positions['C8'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))

        # Edge moves
        Positions['E10'].pos = vector(EdgDecPos, -1-dis, -EdgIncPos)
        Positions['E10'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['E9'].pos = vector(EdgIncPos, -1-dis, EdgDecPos)
        Positions['E9'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['E11'].pos = vector(-EdgIncPos, -1-dis, -EdgDecPos)
        Positions['E11'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))
        Positions['E12'].pos = vector(-EdgDecPos, -1-dis, EdgIncPos)
        Positions['E12'].rotate(axis=vector(0,1,0), angle=convert_to_radius(1))

    # Change cubies positions
    Positions['C5'], Positions['C6'], Positions['C7'], Positions['C8'] = Positions['C6'], Positions['C8'], Positions['C5'], Positions['C7']
    Positions['E9'], Positions['E10'], Positions['E11'], Positions['E12'] = Positions['E12'], Positions['E9'], Positions['E10'], Positions['E11']

    # Recalling the Function for moves with a 2
    if turn == 2:
        D_move(1)

# D' move
def dpr_move(x):
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenY.rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))

        # Corners moves
        Positions['C5'].pos = vector(CorChangePos, -1-dis, CorBallancePos)
        Positions['C5'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['C7'].pos = vector(CorBallancePos, -1-dis, -CorChangePos)
        Positions['C7'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['C6'].pos = vector(-CorBallancePos, -1-dis, CorChangePos)
        Positions['C6'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['C8'].pos = vector(-CorChangePos, -1-dis, -CorBallancePos)
        Positions['C8'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))

        # Edge moves
        Positions['E10'].pos = vector(EdgDecPos, -1-dis, EdgIncPos)
        Positions['E10'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['E9'].pos = vector(-EdgIncPos, -1-dis, EdgDecPos)
        Positions['E9'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['E11'].pos = vector(EdgIncPos, -1-dis, -EdgDecPos)
        Positions['E11'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))
        Positions['E12'].pos = vector(-EdgDecPos, -1-dis, -EdgIncPos)
        Positions['E12'].rotate(axis=vector(0,1,0), angle=convert_to_radius(-1))

    # Change cubies positions
    Positions['C5'], Positions['C6'], Positions['C7'], Positions['C8'] = Positions['C7'], Positions['C5'], Positions['C8'], Positions['C6']
    Positions['E9'], Positions['E10'], Positions['E11'], Positions['E12'] = Positions['E10'], Positions['E11'], Positions['E12'], Positions['E9']

# F move
def f_move(turn):
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenG.rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))

        # Corners moves
        Positions['C1'].pos = vector(CorBallancePos, CorChangePos, 1+dis)
        Positions['C1'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['C2'].pos = vector(-CorChangePos, CorBallancePos, 1+dis)
        Positions['C2'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['C5'].pos = vector(CorChangePos, -CorBallancePos, 1+dis)
        Positions['C5'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['C6'].pos = vector(-CorBallancePos, -CorChangePos, 1+dis)
        Positions['C6'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))

        # Edge moves
        Positions['E1'].pos = vector(EdgIncPos, EdgDecPos, 1+dis)
        Positions['E1'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['E5'].pos = vector(EdgDecPos, -EdgIncPos, 1+dis)
        Positions['E5'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['E6'].pos = vector(-EdgDecPos, EdgIncPos, 1+dis)
        Positions['E6'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
        Positions['E9'].pos = vector(-EdgIncPos, -EdgDecPos, 1+dis)
        Positions['E9'].rotate(axis=vector(0,0,1), angle=convert_to_radius(-1))
    
    # Change cubies positions
    Positions['C1'], Positions['C2'], Positions['C5'], Positions['C6'] = Positions['C2'], Positions['C6'], Positions['C1'], Positions['C5']
    Positions['E1'], Positions['E5'], Positions['E6'], Positions['E9'] = Positions['E6'], Positions['E1'], Positions['E9'], Positions['E5']

    # Recalling the Function for moves with a 2
    if turn == 2:
        F_move(1)

# F' move
def fpr_move(x):
    for CorBallancePos, CorChangePos, EdgIncPos, EdgDecPos in zip(CorBallancePositions, CorChangePositions, EdgIncPositions, EdgDecPositions): # all list lengths are 90 Bcause of rotatins
        rate(150)
        # Center move
        CenG.rotate(axis=vector(0,0,1), angle=convert_to_radius(1))

        # Corners moves
        Positions['C1'].pos = vector(CorChangePos, CorBallancePos, 1+dis)
        Positions['C1'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['C2'].pos = vector(-CorBallancePos, CorChangePos, 1+dis)
        Positions['C2'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['C5'].pos = vector(CorBallancePos, -CorChangePos, 1+dis)
        Positions['C5'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['C6'].pos = vector(-CorChangePos, -CorBallancePos, 1+dis)
        Positions['C6'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))

        # Edge moves
        Positions['E1'].pos = vector(-EdgIncPos, EdgDecPos, 1+dis)
        Positions['E1'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['E5'].pos = vector(EdgDecPos, EdgIncPos, 1+dis)
        Positions['E5'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['E6'].pos = vector(-EdgDecPos, -EdgIncPos, 1+dis)
        Positions['E6'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
        Positions['E9'].pos = vector(EdgIncPos, -EdgDecPos, 1+dis)
        Positions['E9'].rotate(axis=vector(0,0,1), angle=convert_to_radius(1))
    
    # Change cubies positions
    Positions['C1'], Positions['C2'], Positions['C5'], Positions['C6'] = Positions['C5'], Positions['C1'], Positions['C6'], Positions['C2']
    Positions['E1'], Positions['E5'], Positions['E6'], Positions['E9'] = Positions['E5'], Positions['E9'], Positions['E1'], Positions['E6']

# Button widgets
button(bind=R_move, text="  R  ", background=color.red, color=color.black)
scene.append_to_caption('\t')
button(bind=Rpr_move, text="  R'  ", background=color.red, color=color.black)
scene.append_to_caption('\t')
button(bind=lambda: R_move(2), text="  R2  ", background=color.red, color=color.black)
scene.append_to_caption('\n\n')

button(bind=U_move, text="  U  ", background=color.white, color=color.black)
scene.append_to_caption('\t')
button(bind=Upr_move, text="  U'  ", background=color.white, color=color.black)
scene.append_to_caption('\t')
button(bind=lambda: U_move(2), text="  U2  ", background=color.white, color=color.black)
scene.append_to_caption('\n\n')

button(bind=B_move, text="  B  ", background=color.blue, color=color.white)
scene.append_to_caption('\t')
button(bind=Bpr_move, text="  B'  ", background=color.blue, color=color.white)
scene.append_to_caption('\t')
button(bind=lambda: B_move(2), text="  B2  ", background=color.blue, color=color.white)
scene.append_to_caption('\n\n')

button(bind=L_move, text="  L  ", background=color.orange, color=color.black)
scene.append_to_caption('\t')
button(bind=Lpr_move, text="  L'  ", background=color.orange, color=color.black)
scene.append_to_caption('\t')
button(bind=lambda: L_move(2), text="  L2  ", background=color.orange, color=color.black)
scene.append_to_caption('\n\n')

button(bind=D_move, text="  D  ", background=color.yellow, color=color.black)
scene.append_to_caption('\t')
button(bind=Dpr_move, text="  D'  ", background=color.yellow, color=color.black)
scene.append_to_caption('\t')
button(bind=lambda: D_move(2), text="  D2  ", background=color.yellow, color=color.black)
scene.append_to_caption('\n\n')

button(bind=F_move, text="  F  ", background=color.green, color=color.black)
scene.append_to_caption('\t')
button(bind=Fpr_move, text="  F'  ", background=color.green, color=color.black)
scene.append_to_caption('\t')
button(bind=lambda: F_move(2), text="  F2  ", background=color.green, color=color.black)


# preventing pauses in the program
while True:
    pass
