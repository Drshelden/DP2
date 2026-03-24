#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc
import math

import System
import System.Collections.Generic
import Rhino


rs.SetStickyInteger("DRS_Entry", "DRS", 5)
value = rs.GetStickyInteger("DRS_Entry", "DRS", 0)
print(str(value))
