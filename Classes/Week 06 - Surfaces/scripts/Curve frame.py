#! python3
import rhinoscriptsyntax as rs
import Rhino
import numpy

import Rhino 
import rhinoscriptsyntax as rs 
import scriptcontext as sc 
id = rs.GetObject("Select curve", rs.filter.curve) 
t = rs.GetReal(message="t parameter", minimum=0.0, maximum=1.0)
if (id): 
    curve = rs.coercecurve(id) 
    if curve: 
        t = curve.Domain.Min + (curve.Domain.Max - curve.Domain.Min) * t
        pt = curve.PointAt(t) 
        sc.doc.Objects.AddPoint(pt) 
        rs.AddPoint(pt) 
        
        # Calculate curvature
        curvature_vector = curve.CurvatureAt(t)
        curvature = curvature_vector.Length  # Magnitude of curvature vector
        
        # Calculate torsion using derivatives
        d1 = curve.DerivativeAt(t, 1)  # First derivative (tangent)
        d2 = curve.DerivativeAt(t, 2)  # Second derivative
        d3 = curve.DerivativeAt(t, 3)  # Third derivative
        
        # Torsion formula: τ = (r' × r'') · r''' / |r' × r''|²
        cross_d1_d2 = Rhino.Geometry.Vector3d.CrossProduct(d1, d2)
        cross_magnitude_squared = cross_d1_d2.SquareLength
        
        if cross_magnitude_squared > 1e-10:  # Avoid division by zero
            torsion = Rhino.Geometry.Vector3d.Multiply(cross_d1_d2, d3) / cross_magnitude_squared
        else:
            torsion = 0.0
        
        # Print results
        print("Point at t={}: {}".format(t, pt))
        print("Curvature: {:.6f}".format(curvature))
        print("Torsion: {:.6f}".format(torsion))
        
        rc, plane = curve.FrameAt(t) 
        dom = Rhino.Geometry.Interval(0.0, 5.0) 
        srf = Rhino.Geometry.PlaneSurface(plane, dom, dom) 
        sc.doc.Objects.AddSurface(srf) 
        sc.doc.Views.Redraw();
