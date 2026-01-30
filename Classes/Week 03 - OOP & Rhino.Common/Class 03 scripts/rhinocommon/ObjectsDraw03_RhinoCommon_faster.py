import time
import Rhino
import scriptcontext as sc

xCount = yCount = zCount = 10
xScale = yScale = zScale = 5
rSphere = 5
xOffset = 0
time_start = time_mid = time_end = time.time()

def MakeSpheres():
    """Create a grid of spheres using Rhino.Common with disabled redraw"""
    global time_start, time_mid, time_end
    
    # Disable redraw for faster performance
    sc.doc.Views.RedrawEnabled = False
    time_start = time.time()
    
    try:
        for x in range(xCount):
            for y in range(yCount):
                for z in range(zCount):
                    pt = Rhino.Geometry.Point3d(x * xScale + xOffset, y * yScale, z * zScale)
                    sc.doc.Objects.AddSphere(Rhino.Geometry.Sphere(pt, rSphere))
        time_mid = time.time()
    finally:
        # Re-enable redraw
        sc.doc.Views.RedrawEnabled = True
        sc.doc.Views.Redraw()
    time_end = time.time()

if __name__=="__main__":
    # Create spheres (redraw disabled during this)
    MakeSpheres()
    
    # Calculate elapsed times
    elapsed_time1 = time_mid - time_start
    elapsed_time2 = time_end - time_mid
    
    # Print results only after all spheres are added and screen is refreshed
    print("-" * 40)
    print("Rhino.Common Sphere Grid Creation")
    print("(With Disabled Redraw - Fastest)")
    print("-" * 40)
    print("Geometry Creation Time: {:.4f} seconds".format(elapsed_time1))
    print("Redraw Time: {:.4f} seconds".format(elapsed_time2))
    print("-" * 40)
