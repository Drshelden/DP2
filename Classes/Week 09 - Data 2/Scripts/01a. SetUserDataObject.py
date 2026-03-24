#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc
import math

import System
import System.Collections.Generic
import Rhino


object = rs.GetObject(message=None, filter=0, preselect=True, select=True, subobjects=True)
x = rs.coercebrep(object)
x.UserDictionary.Set("DRS", 5)  # <-- TM removed!
_, value = x.UserDictionary.TryGetValue("DRS")
print(str(value))