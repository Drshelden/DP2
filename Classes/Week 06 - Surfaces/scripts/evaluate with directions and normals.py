import rhinoscriptsyntax as rs
import scriptcontext as sc
import math
import numpy

import System
import System.Collections.Generic
import Rhino

# s, u, v are provided by Grasshopper inputs

print("U Domain: ", s.Domain(0).Min, " to: ", s.Domain(0).Max )
print("V Domain: ", s.Domain(1).Min, " to: ", s.Domain(1).Max )
print("U Degree: ", s.Degree(0) )
print("V Degree: ", s.Degree(1) )

# Evaluate point at UV
Puv = s.PointAt(u, v)

# Get isocurves
Cu = s.IsoCurve(1, u)
Cv = s.IsoCurve(0, v)

# Compute partial derivatives (tangent vectors) from isocurves
# The tangent to the U-isocurve at this point is the V-direction tangent
# The tangent to the V-isocurve at this point is the U-direction tangent
param_u_on_Cu = Cu.Domain.ParameterAt(0.0) if Cu.Domain.Min == v else Cu.ClosestPoint(Puv)[1]
param_v_on_Cv = Cv.Domain.ParameterAt(0.0) if Cv.Domain.Min == u else Cv.ClosestPoint(Puv)[1]

tangent_v = Cu.TangentAt(param_u_on_Cu)  # Tangent along U-isocurve = V direction
tangent_u = Cv.TangentAt(param_v_on_Cv)  # Tangent along V-isocurve = U direction

# Compute surface normal (cross product of tangents)
normal = Rhino.Geometry.Vector3d.CrossProduct(tangent_u, tangent_v)
normal.Unitize()

# Compute principal curvatures and directions
rc, frame = s.FrameAt(u, v)
principal_dir1 = frame.XAxis  # First principal direction
principal_dir2 = frame.YAxis  # Second principal direction

# Get principal curvatures
curvature = s.CurvatureAt(u, v)
if curvature:
    kappa_u = curvature.Kappa(0)  # Principal curvature in first direction
    kappa_v = curvature.Kappa(1)  # Principal curvature in second direction
    
    print("\nPrincipal Curvatures:")
    print("Kappa 1: {:.6f}".format(kappa_u))
    print("Kappa 2: {:.6f}".format(kappa_v))

# Scale factor for visualization
scale = 2.0

# Create lines for tangent vectors
tangent_u_normalized = Rhino.Geometry.Vector3d(tangent_u)
tangent_u_normalized.Unitize()
line_tangent_u = Rhino.Geometry.Line(Puv, Puv + tangent_u_normalized * scale)

tangent_v_normalized = Rhino.Geometry.Vector3d(tangent_v)
tangent_v_normalized.Unitize()
line_tangent_v = Rhino.Geometry.Line(Puv, Puv + tangent_v_normalized * scale)

# Create line for normal vector
line_normal = Rhino.Geometry.Line(Puv, Puv + normal * scale)

# Create lines for principal directions
line_principal1 = Rhino.Geometry.Line(Puv, Puv + principal_dir1 * scale)
line_principal2 = Rhino.Geometry.Line(Puv, Puv + principal_dir2 * scale)

print("\nVectors computed:")
print("- Tangent U (∂S/∂u): ", tangent_u)
print("- Tangent V (∂S/∂v): ", tangent_v)
print("- Normal: ", normal)
print("- Principal Direction 1: ", principal_dir1)
print("- Principal Direction 2: ", principal_dir2)

# Output to Grasshopper
T_u = line_tangent_u
T_v = line_tangent_v
N = line_normal
P1 = line_principal1
P2 = line_principal2