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


xCount = 10
yCount = 10
zCount = 5
xScale = 10
yScale = 10
zScale = 10
rSphere = 2

thetaValues = np.arange(0, 2 * math.pi, 2 * math.pi /xCount) # 0 to 2PI in xCount steps
alphaValues = np.arange(0, math.pi / 2.0, math.pi / yCount) # 0 to PI / 2 in yCount steps

pointIds = []


# Print out the coordinates of each point
i = 0

pointIds = [[0 for _ in range(16)] for _ in range(16)]

for theta in thetaValues:
    j = 0
    for alpha in alphaValues:

        x = math.cos(theta) * math.cos(alpha)
        y = math.sin(theta) * math.cos(alpha)
        z = math.sin(alpha)

        pointId = rs.AddPoint( (x * xScale, y * yScale, z * zScale) )
        pointIds[i][j] = pointId
        if (i > 0): rs.AddLine(pointIds[i-1][j], pointIds[i][j])
        if (j > 0): rs.AddLine(pointIds[i][j-1], pointIds[i][j])

        #sphereId = rs.AddSphere( (x * xScale, y * yScale, z * zScale), rSphere )
        #print(sphereId)
        #rs.ObjectColor(sphereId, [int(random.random() * 255), int(random.random() * 255), int(random.random() * 255) ])

        j = j + 1
    i = i + 1

 # done!