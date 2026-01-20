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
zCount = 10
xScale = 10
yScale = 10
zScale = 10
rSphere = 5


# Print out the coordinates of each point
for x in range(xCount):
    for y in range(yCount):
        pointId = rs.AddPoint((x * xScale, y * yScale,0))
        print(x, y, pointId)         

 # done!