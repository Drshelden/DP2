#! python3
"""Testing pip install specific packages"""
# r: numpy

import rhinoscriptsyntax as rs
import scriptcontext as sc

import System
import System.Collections.Generic
import Rhino
import random
import math
import numpy as np


xCount = 16.0
yCount = 10.0
zCount = 5
xScale = 10
yScale = 10
zScale = 10
rSphere = 2

thetaValues = np.arange(0, 2 * math.pi, 2 * math.pi /xCount) # 0 to 2PI in 16 steps
alphaValues = np.arange(0, math.pi / 2.0, math.pi / 2.0 / yCount) # 0 to 1 in 0.1 steps
print(len(thetaValues), " " , len(alphaValues))

pointIds = []
sphereIds = []


# Print out the coordinates of each point
i = 0

pointIds = [[0 for _ in range(len(alphaValues))] for _ in range(len(thetaValues))]

for theta in thetaValues:
    j = 0
    for alpha in alphaValues:

        x = math.cos(theta) * math.cos(alpha)
        y = math.sin(theta) * math.cos(alpha)
        z = math.sin(alpha)

        pointId = rs.AddPoint( (x * xScale, y * yScale, z * zScale) )
        print (i, " " , j)
        pointIds[i][j] = pointId

        sphereId = rs.AddSphere( (x * xScale, y * yScale, z * zScale), rSphere )
        sphereIds.append(sphereId)
        #print(sphereId)
        #rs.ObjectColor(sphereId, [int(random.random() * 255), int(random.random() * 255), int(random.random() * 255) ])

        j = j + 1
    i = i + 1

newSphereId = rs.AddSphere( (0,0,0), xScale )

rs.BooleanDifference(newSphereId, sphereIds)

 # done!