#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n.
    Returns an empty list if n <= 0.
    """
    # Initialize an empty list for Pascal's Triangle
    triangle = []
    
    # Return empty list if n is less than or equal to 0
    if n <= 0:
        return triangle

    # Start the triangle with the first row [1]
    triangle = [[1]]

    # Generate the remaining rows
    for i in range(1, n):
        # Create a new row starting with [1]
        row = [1]
        
        # Fill in the middle values by adding adjacent elements from the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # End each row with [1]
        row.append(1)
        
        # Append the row to the triangle
        triangle.append(row)

    return triangle
