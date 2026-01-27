
#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc
import math

import System
import System.Collections.Generic
import Rhino

geoPoint = rs.CreatePoint(10.0, 20.0, 30.0)
print("geoPoint is a: " + str(type(geoPoint))) # this is a "Point3d"

rhinoPointGUID = rs.AddPoint(geoPoint)
print("rhinoPoint is a: " + str(type(rhinoPointGUID))) # this is a GUID pointer to a point in rhino.

lineGUID = rs.AddLine(geoPoint,(110.0, 20.0, 30.0))
#lineGUID = rs.AddLine(rhinoPointGUID,(110.0, 20.0, 30.0))
 
print(lineGUID)


sc.doc = Rhino.RhinoDoc.ActiveDoc
obj = sc.doc.Objects.Find(lineGUID)
print("object is: " + str(obj))

obj.Attributes.ObjectColor = rs.CreateColor(128, 0, 0)

ptColorObj = obj.Attributes.ObjectColor
print(ptColorObj)
print("Alpha Value = ", ptColorObj.A)
print("R Value = ", ptColorObj.R)
print("G Value = ", ptColorObj.G)
print("B Value = ", ptColorObj.B)
 


