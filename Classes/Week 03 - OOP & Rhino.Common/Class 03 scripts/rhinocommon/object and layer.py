
#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc
import math

import System
import System.Collections.Generic
import Rhino

geoPoint = rs.CreatePoint(10.0, 20.0, 30.0)
print("geoPoint is a: " + str(type(geoPoint))) # this is a "Point3d"


#rs.AddPoint((0,0,0))

rhinoPointGUID = rs.AddPoint(geoPoint)
print("rhinoPoint is a: " + str(type(rhinoPointGUID))) # this is a GUID pointer to a point in rhino.

#rhinoPointObject = rhinoPointGUID.Object()
#print(rhinoPointGUID.Attributes.LayerIndex)

sc.doc = Rhino.RhinoDoc.ActiveDoc
obj = sc.doc.Objects.Find(rhinoPointGUID)
attr = obj.Attributes
index = obj.Attributes.LayerIndex
print(index)


