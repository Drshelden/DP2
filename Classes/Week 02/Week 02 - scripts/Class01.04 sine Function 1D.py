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


xCount = 16
yCount = 5
zCount = 5
xScale = 10
yScale = 10
zScale = 10
rSphere = 5

listValues = np.arange(0, 2 * math.pi, 2 * math.pi / xCount)
print(listValues)

# Print out the coordinates of each point
for x in listValues:

        y = 2.0 *  math.cos(x / 2.0)
        
        sphereId = rs.AddSphere( (x * xScale, y * yScale, 0), rSphere )
        #print(sphereId)
        rs.ObjectColor(sphereId, [int(random.random() * 255), int(random.random() * 255), int(random.random() * 255) ])               

 # done!