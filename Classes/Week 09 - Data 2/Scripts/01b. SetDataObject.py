#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc
import math

import System
import System.Collections.Generic
import Rhino


object = rs.GetObject(message=None, filter=0, preselect=True, select=True, subobjects=True)


value = rs.GetUserText(object, "DRS2")
print(str(value))
