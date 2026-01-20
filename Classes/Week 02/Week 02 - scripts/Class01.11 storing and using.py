import rhinoscriptsyntax as rs

def create_connected_grid():
    # ------------------------------------------------------------------
    # SETUP
    # ------------------------------------------------------------------
    xCount = 5
    yCount = 5
    spacing = 10
    radius = 2

    # Disable redraw for performance (script runs faster without updating viewport every step)
    rs.EnableRedraw(False)

    # ------------------------------------------------------------------
    # STEP 1: INITIALIZATION (Pre-allocation)
    # ------------------------------------------------------------------
    # Create an empty matrix structure (List of Lists) filled with None.
    # This defines the "shelves" before we put the books on them.
    point_matrix = []

    for x in range(xCount):
        # Create a row of empty slots
        empty_row = [None] * yCount
        # Add the row to the main matrix
        point_matrix.append(empty_row)

    # ------------------------------------------------------------------
    # STEP 2: POPULATION
    # ------------------------------------------------------------------
    # Iterate through the dimensions to create geometry and store the points.
    for x in range(xCount):
        for y in range(yCount):
            
            # Create point coordinate
            pt = (x * spacing, y * spacing, 0)
            
            # Add point to Rhino and get its ID
            pt_id = rs.AddPoint(pt)
            
            # Store the point coordinate (not the ID) for later use
            point_matrix[x][y] = pt

    # ------------------------------------------------------------------
    # STEP 3: UTILIZATION (Connectivity)
    # ------------------------------------------------------------------
    # Iterate through the matrix again to draw connections based on grid neighbors.
    for x in range(xCount):
        for y in range(yCount):
            
            # Retrieve the current point from storage
            current_pt = point_matrix[x][y]
            
            # Connect to previous neighbor in X direction (Look Backwards)
            if x > 0:
                prev_x_pt = point_matrix[x-1][y]
                if prev_x_pt: # Check if point exists
                    rs.AddLine(current_pt, prev_x_pt)
            
            # Connect to previous neighbor in Y direction (Look Backwards)
            if y > 0:
                prev_y_pt = point_matrix[x][y-1]
                if prev_y_pt: # Check if point exists
                    rs.AddLine(current_pt, prev_y_pt)

    # ------------------------------------------------------------------
    # CLEANUP
    # ------------------------------------------------------------------
    rs.EnableRedraw(True)
    print("Generated " + str(xCount * yCount) + " points and connections.")

# Execution
if __name__ == "__main__":
    create_connected_grid()