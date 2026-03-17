#! python3
# getDocumentData.py

import rhinoscriptsyntax as rs
value = rs.GetDocumentData("DRS", "MyEntry1")
print(value)
value = rs.GetDocumentData("DRS", "MyEntry2")
print(value)
value = rs.GetDocumentData("DRS", "MyEntry3")
print(value)