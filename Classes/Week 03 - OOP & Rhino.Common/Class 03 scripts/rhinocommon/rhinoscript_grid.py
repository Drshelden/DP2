import time
import Rhino
import scriptcontext as sc
import rhinoscriptsyntax as rs

xCount = yCount = zCount = 5
xScale = yScale = zScale = 5
rSphere = 5

def MakeSpheres(isCommon, redraw=False):
    # 1. DISABLE REDRAW: This stops Rhino from meshing/rendering between steps
    sc.doc.Views.RedrawEnabled = False
    
    # Use a try/finally block to ensure Redraw is turned back on even if code fails
    try:
        for x in range(xCount):
            for y in range(yCount):
                for z in range(zCount):
                    pt = Rhino.Geometry.Point3d(x * xScale + xOffset, y * yScale, z * zScale)
                    
                    if isCommon:
                        # Rhino Common method (Fast, direct to DB)
                        sc.doc.Objects.AddSphere(Rhino.Geometry.Sphere(pt, rSphere))
                    else:
                        # RhinoScript syntax method (Slower, wraps Common)
                        rs.AddSphere(pt, rSphere)
                        
    finally:
        # 2. RE-ENABLE REDRAW: Restore view updates after all math is done
        sc.doc.Views.RedrawEnabled = True
    
    # 3. FORCE UPDATE: Only redraw once at the very end if requested
    if redraw:
        sc.doc.Views.Redraw()

if __name__=="__main__":
    # --- Test 1: Common (Fastest) ---
    xOffset = 0
    time0 = time.time()
    MakeSpheres(isCommon=True, redraw=False)
    time1 = time.time()
    elapsedTime0 = time1 - time0

    # --- Test 2: Common with Redraw (Fast w/ visual update at end) ---
    xOffset += (xCount + 1) * xScale
    MakeSpheres(isCommon=True, redraw=True)
    time2 = time.time()
    elapsedTime1 = time2 - time1

    # --- Test 3: RhinoScript (Slowest) ---
    xOffset += (xCount + 1) * xScale
    MakeSpheres(isCommon=False, redraw=True) 
    time3 = time.time()
    elapsedTime2 = time3 - time2

    print("-" * 30)
    # Using .format() instead of f-strings for compatibility
    print("Common (No Redraw): {:.4f} sec".format(elapsedTime0))
    print("Common (W/ Redraw): {:.4f} sec".format(elapsedTime1))
    print("RhinoScript       : {:.4f} sec".format(elapsedTime2))