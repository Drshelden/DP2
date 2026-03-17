#! python3
# setUserText.py

import rhinoscriptsyntax as rs
ref = rs.GetObject("select the object")

rs.SetUserText(ref, "MyEntry1", "1")
rs.SetUserText(ref, "MyEntry2", "bird")
rs.SetUserText(ref, "MyEntry3", "blue")

