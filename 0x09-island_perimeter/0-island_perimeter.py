#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list): A list of lists of integers representing the grid, where
                     0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # It's land
                # Check the four directions
                if i == 0 or grid[i - 1][j] == 0:  # Check upwards
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Check downwards
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Check leftwards
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Check rightwards
                    perimeter += 1

    return perimeter                      
