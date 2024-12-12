#!/usr/bin/python3
"""
Function to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Function to calculate the perimeter of the island described in the grid.

    Parameters:
    grid (list of list of integers): The 2D grid representing the island map.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Iterate through the grid to check every land cell
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # This is land
                # Check all four possible edges
                # Top edge
                if i == 0 or grid[i-1][j] == 0:  # Out of bounds or water
                    perimeter += 1
                # Bottom edge
                if i == rows - 1 or grid[i+1][j] == 0:  # Out of bounds||water
                    perimeter += 1
                # Left edge
                if j == 0 or grid[i][j-1] == 0:  # Out of bounds or water
                    perimeter += 1
                # Right edge
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
