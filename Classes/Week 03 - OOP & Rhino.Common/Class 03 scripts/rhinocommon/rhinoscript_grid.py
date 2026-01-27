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
import time
xCount = yCount = zCount = 10
xScale = yScale = zScale = 10
rSphere = 5
def MakeSpheres(isCommon, redraw = False):
  for x in range(xCount):
    for y in range(yCount):
      for z in range(zCount):
        if (isCommon):
          sc.doc.Objects.AddSphere(Rhino.Geometry.Sphere \
            (Rhino.Geometry.Point3d(x * xScale + xOffset, y * yScale,z * zScale), rSphere))
        if (redraw): 
            sc.doc.Views.Redraw()
        else:
            rs.AddSphere((x * xScale + xOffset, y * yScale,z * zScale), rSphere)

if __name__=="__main__":
    xOffset = 0
    time0 = time.time()
    MakeSpheres(True, False)
    time1 = time.time()
    elapsedTime0 = time1 - time0

    xOffset += (xCount + 1) * xScale
    MakeSpheres(True, True)
    time2 = time.time()
    elapsedTime1 = time2 - time1

    xOffset += (xCount + 1) * xScale
    MakeSpheres(False)
    time3 = time.time()
    elapsedTime2 = time3 - time2

    print("Times: common without redraw:", elapsedTime0, "\ncommon with redraw:", 
	elapsedTime1, "rhinoscript:", elapsedTime2)