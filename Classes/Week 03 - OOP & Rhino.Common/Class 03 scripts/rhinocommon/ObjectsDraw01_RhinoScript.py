import time
import Rhino
import scriptcontext as sc
import rhinoscriptsyntax as rs

xCount = yCount = zCount = 5
xScale = yScale = zScale = 5
rSphere = 5
xOffset = 0
time_start = time_mid = time_end = time.time()

def MakeSpheres():
    """Create a grid of spheres using RhinoScript (rs.AddSphere)"""
    global time_start, time_mid, time_end
    
    time_start = time.time()
    
    for x in range(xCount):
        for y in range(yCount):
            for z in range(zCount):
                pt = [x * xScale + xOffset, y * yScale, z * zScale]
                rs.AddSphere(pt, rSphere)
    
    time_mid = time.time()

if __name__=="__main__":
    # Create spheres
    MakeSpheres()
    
    # Measure time after redraw
    time_end = time.time()
    
    # Calculate elapsed times
    elapsed_time1 = time_mid - time_start
    elapsed_time2 = time_end - time_mid
    
    print("-" * 40)
    print("RhinoScript rs.AddSphere Grid Creation")
    print("-" * 40)
    print("Geometry Creation Time: {:.4f} seconds".format(elapsed_time1))
    print("Total Time (incl. redraw): {:.4f} seconds".format(elapsed_time1 + elapsed_time2))
    print("-" * 40)
