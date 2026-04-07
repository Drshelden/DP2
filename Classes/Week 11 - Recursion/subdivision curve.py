import rhinoscriptsyntax as rs

def chaikin_subdivision(points, iterations):
    """Perform Chaikin's subdivision on a set of points."""
    for _ in range(iterations):
        new_points = []
        
        # Iterate through pairs of points
        for i in range(len(points) - 1):
            p0 = points[i]
            p1 = points[i + 1]
            
            # Compute the new points using Chaikin's algorithm
            q = [(3 * p0[0] + p1[0]) / 4, (3 * p0[1] + p1[1]) / 4, (3 * p0[2] + p1[2]) / 4]
            r = [(p0[0] + 3 * p1[0]) / 4, (p0[1] + 3 * p1[1]) / 4, (p0[2] + 3 * p1[2]) / 4]
            
            new_points.append(q)
            new_points.append(r)
        
        # Add the last point of the polyline
        new_points.append(points[-1])
        
        # Update points for the next iteration
        points = new_points
    
    return points

def main():
    """Main function to create a subdivision curve in Rhino."""
    
    # Select a polyline
    polyline = rs.GetObject("Select a polyline to subdivide", rs.filter.curve)
    if not polyline or rs.CurveDegree(polyline) != 1:
        print("Please select a valid polyline.")
        return
    
    # Get number of subdivision iterations
    iterations = rs.GetInteger("Enter number of subdivision iterations", 3, 1, 10)
    if iterations is None:
        return
    
    # Get the polyline points
    points = rs.CurvePoints(polyline)
    
    # Perform Chaikin subdivision
    smooth_points = chaikin_subdivision(points, iterations)
    
    # Create the new subdivision curve
    new_curve = rs.AddPolyline(smooth_points)
    
    if new_curve:
        rs.SelectObject(new_curve)
        print(f"Subdivision curve created with {iterations} iterations.")
    else:
        print("Failed to create the subdivision curve.")

# Run the script
if __name__ == "__main__":
    main()
