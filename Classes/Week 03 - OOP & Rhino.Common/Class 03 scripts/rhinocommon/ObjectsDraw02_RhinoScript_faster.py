import time
import Rhino
import scriptcontext as sc
import rhinoscriptsyntax as rs

xCount = yCount = zCount = 10
xScale = yScale = zScale = 5
rSphere = 5
xOffset = 0
time_start = time_mid = time_end = time.time()

def MakeSpheres():
    """Create a grid of spheres using RhinoScript (rs.AddSphere) with disabled redraw"""
    global time_start, time_mid, time_end
    
    # Disable redraw for faster performance
    sc.doc.Views.RedrawEnabled = False
    time_start = time.time()   
    try:
        for x in range(xCount):
            for y in range(yCount):
                for z in range(zCount):
                    pt = [x * xScale + xOffset, y * yScale, z * zScale]
                    rs.AddSphere(pt, rSphere)
        time_mid = time.time()
    finally:
        # Re-enable redraw
        sc.doc.Views.RedrawEnabled = True
        sc.doc.Views.Redraw()
    time_end = time.time() 
if __name__=="__main__":
    # Measure time at start
    
    
    # Create spheres (redraw disabled during this)
    MakeSpheres()
    
    # Measure time at end
    
    
    # Calculate elapsed time
    elapsed_time1 = time_mid - time_start
    elapsed_time2 = time_end - time_mid

    # Print results only after all spheres are added and screen is refreshed
    print("-" * 40)
    print("RhinoScript rs.AddSphere Grid Creation")
    print("(With Disabled Redraw - Faster)")
    print("-" * 40)
    print("Geometry Creation Time: {:.4f} seconds".format(elapsed_time1))
    print("Redraw Time: {:.4f} seconds".format(elapsed_time2))
    print("-" * 40)
