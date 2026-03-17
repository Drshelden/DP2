#! python3
# setDocumentData.py

import rhinoscriptsyntax as rs
print(rs.GetDocumentData("DRS", "MyEntry1"))
print(rs.GetDocumentData("DRS", "MyEntry2"))
print(rs.GetDocumentData("DRS", "MyEntry3"))
