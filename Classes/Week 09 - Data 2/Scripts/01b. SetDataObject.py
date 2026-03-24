#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc
import math

import System
import System.Collections.Generic
import Rhino


object = rs.GetObject(message=None, filter=0, preselect=True, select=True, subobjects=True)
rs.SetUserData(object, "DRS", 5)
value = rs.GetUserData(object, "DRS")
print(str(value))
