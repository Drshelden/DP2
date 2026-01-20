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
rSphere = 5


# Print out the coordinates of each point
for x in range(xCount):
    for y in range(yCount):
            for z in range(zCount):
                pointId = rs.AddPoint((x * xScale, y * yScale,z * zScale))
                print(x, y, pointId)      

                if (random.random() < 0.25):   
                    sphereId= rs.AddSphere((x * xScale, y * yScale,z * zScale), rSphere)
                    rs.ObjectColor(sphereId, [int(random.random() * 255), int(random.random() * 255), \
                    int(random.random() * 255) ])

 # done!