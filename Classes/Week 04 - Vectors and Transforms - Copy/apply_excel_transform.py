"""
Rhino Script: Apply Excel Transform to Selected Objects

This script (Python 3 compatible):
1. Reads a 4x4 region from Excel via clipboard
2. Validates that it's 4x4 and contains numerical values
3. Creates a Transform from the matrix
4. Applies it to all selected objects in Rhino

Author: Rhino Script Assistant
Date: February 2026
"""

import rhinoscriptsyntax as rs
import Rhino
from Rhino.Geometry import Transform
import subprocess

def get_excel_matrix():
    """
    Read a 4x4 matrix from the clipboard (copied from Excel).
    User should select a 4x4 range in Excel, copy it (Ctrl+C), then run this script.
    Returns: A 4x4 list of values, or None if unsuccessful
    """
    try:
        # Get clipboard contents
        result = subprocess.check_output(
            ['powershell', '-Command', 'Get-Clipboard']
        )
        
        # Decode bytes to string
        if isinstance(result, bytes):
            clipboard_data = result.decode('utf-8').strip()
        else:
            clipboard_data = str(result).strip()
        
        if not clipboard_data:
            print("Error: Clipboard is empty.")
            print("Please select a 4x4 range in Excel, copy it (Ctrl+C), and try again.")
            return None
        
        # Parse the clipboard data (Excel copies with tabs and newlines)
        lines = clipboard_data.strip().split('\n')
        
        # Check if we have 4 rows
        if len(lines) != 4:
            print("Error: Clipboard data is not 4 rows.")
            print("Please select a 4x4 range in Excel and try again.")
            print("Current rows: {}".format(len(lines)))
            return None
        
        # Parse the matrix
        matrix = []
        for row_idx, line in enumerate(lines):
            # Split by tabs (Excel's default copy format)
            values = line.split('\t')
            
            # Check if we have 4 columns
            if len(values) != 4:
                print("Error: Row {} does not have 4 columns.".format(row_idx + 1))
                print("Please select a 4x4 range in Excel and try again.")
                print("Current columns in row {}: {}".format(row_idx + 1, len(values)))
                return None
            
            row = []
            for col_idx, value in enumerate(values):
                try:
                    # Try to convert to float
                    numeric_value = float(value.strip())
                    row.append(numeric_value)
                except (ValueError, TypeError):
                    print("Error: Cell at row {} col {} contains non-numerical value: '{}'".format(
                        row_idx + 1, col_idx + 1, value))
                    return None
            
            matrix.append(row)
        
        print("Successfully read 4x4 matrix from clipboard:")
        for row in matrix:
            print("  " + str(row))
        
        return matrix
    
    except subprocess.CalledProcessError:
        print("Error: Could not read clipboard.")
        print("Please select a 4x4 range in Excel, copy it (Ctrl+C), and try again.")
        return None
    except Exception as e:
        print("Error reading clipboard: " + str(e))
        print("Please select a 4x4 range in Excel, copy it (Ctrl+C), and try again.")
        return None


def matrix_to_transform(matrix):
    """
    Convert a 4x4 matrix to a Rhino Transform object.
    
    Args:
        matrix: A 4x4 list of lists containing numerical values
    
    Returns:
        A Rhino.Geometry.Transform object, or None if unsuccessful
    """
    try:
        # Create a new Transform (identity)
        transform = Transform.Identity
        
        # Set the matrix values using indexers [row, column]
        for row in range(4):
            for col in range(4):
                transform[row, col] = matrix[row][col]
        
        print("Transform created successfully.")
        return transform
    
    except Exception as e:
        print("Error creating Transform: " + str(e))
        return None


def apply_transform_to_selection(transform):
    """
    Apply the transform to copies of all selected objects in Rhino.
    Original objects remain unchanged.
    
    Args:
        transform: A Rhino.Geometry.Transform object
    
    Returns:
        Number of objects transformed, or -1 if unsuccessful
    """
    try:
        # Get selected object IDs
        selected_ids = rs.GetObjects("Select objects to transform", 0, True, True)
        
        if not selected_ids:
            print("No objects selected.")
            return 0
        
        transformed_count = 0
        
        for obj_id in selected_ids:
            try:
                # Copy the object first
                copy_id = rs.CopyObject(obj_id)
                
                if copy_id is None:
                    print("Warning: Could not copy object {}".format(obj_id))
                    continue
                
                # Transform the copy
                result = rs.TransformObject(copy_id, transform)
                
                if result:
                    transformed_count += 1
                else:
                    print("Warning: Could not transform copied object {}".format(copy_id))
            
            except Exception as e:
                print("Error transforming object {}: ".format(obj_id) + str(e))
                continue
        
        print("Successfully created and transformed {} object(s).".format(transformed_count))
        return transformed_count
    
    except Exception as e:
        print("Error during transformation: " + str(e))
        return -1


def main():
    """Main execution function"""
    print("=" * 60)
    print("Rhino Excel Transform Script")
    print("=" * 60)
    print()
    
    # Step 1: Read the 4x4 matrix from Excel
    print("Step 1: Reading 4x4 matrix from Excel...")
    matrix = get_excel_matrix()
    
    if matrix is None:
        print()
        print("Script cancelled.")
        return
    
    print()
    
    # Step 2: Create the Transform
    print("Step 2: Creating Transform...")
    transform = matrix_to_transform(matrix)
    
    if transform is None:
        print()
        print("Script cancelled.")
        return
    
    print()
    
    # Step 3: Apply Transform to selected objects
    print("Step 3: Applying Transform to selected objects...")
    result = apply_transform_to_selection(transform)
    
    if result >= 0:
        print()
        print("=" * 60)
        print("Script completed successfully!")
        print("=" * 60)
    else:
        print()
        print("Script completed with errors.")


# Execute the script
if __name__ == "__main__":
    main()
