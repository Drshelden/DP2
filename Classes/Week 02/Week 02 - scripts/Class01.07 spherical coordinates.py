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


xCount = 5
yCount = 5
zCount = 5
xScale = 10
yScale = 10
zScale = 10
rSphere = 2

thetaValues = np.arange(0, 2 * math.pi, 2 * math.pi /16) # 0 to 2PI in 16 steps
alphaValues = np.arange(0, math.pi / 2.0, math.pi / 16) # 0 to 1 in 0.1 steps


# Print out the coordinates of each point
for theta in thetaValues:
    for alpha in alphaValues:

        x = math.cos(theta) * math.cos(alpha)
        y = math.sin(theta) * math.cos(alpha)
        z = math.sin(alpha)


        sphereId = rs.AddSphere( (x * xScale, y * yScale, z * zScale), rSphere )
        #print(sphereId)
        rs.ObjectColor(sphereId, [int(random.random() * 255), int(random.random() * 255), \
        int(random.random() * 255) ])               

 # done!