#! python3

import rhinoscriptsyntax as rs # this is the rhinoscript library
import scriptcontext as sc # configuration?

import System # standard base python
import System.Collections.Generic #collections specific library
import Rhino # Rhino

# Array points along a curve

    
crv_id = rs.GetObject("Select path curve")
if not crv_id: exit

count = rs.GetInteger("Number of items", 2, 2)
if not count: exit

points = rs.DivideCurve(crv_id, count)
for point in points: rs.AddPoint(point)


