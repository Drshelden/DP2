#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc
import math

import System
import System.Collections.Generic
import Rhino


rs.SetDocumentUserText("DRS", "5")
value = rs.GetDocumentUserText("DRS")
print(str(value))
