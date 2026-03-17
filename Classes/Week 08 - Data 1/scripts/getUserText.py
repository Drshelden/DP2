#! python3
# getUserText.py

import rhinoscriptsyntax as rs
ref = rs.GetObject("select the object")

value = rs.GetUserText(ref, "MyEntry1")
print(value)
value = rs.GetUserText(ref, "MyEntry2")
print(value)
value = rs.GetUserText(ref, "MyEntry3")
print(value)


