#! python3
import rhinoscriptsyntax as rs
import Rhino
import numpy

import Rhino 
import rhinoscriptsyntax as rs 
import scriptcontext as sc 

# Get the surface ID
surface_id = rs.GetObject("Select surface", 8, True)
u = rs.GetReal(message="u parameter", minimum=0.0, maximum=1.0)
v = rs.GetReal(message="v parameter", minimum=0.0, maximum=1.0)

if surface_id:
    # Get the UV parameter
    # u = 0.5
    # v = 0.5
    parameter = [u, v]

    # Get the direction (0 for U, 1 for V)
    direction = 0

    # Extract the isocurve
    curve_ids = rs.ExtractIsoCurve(surface_id, parameter, direction)

    if curve_ids:
        print("Isocurve(s) extracted successfully:")
        for curve_id in curve_ids:
            print(curve_id)
            #rs.AddCurve(curve_id)
    else:
        print("Failed to extract isocurve.")
else:
    print("No surface selected.")
