#!/usr/bin/python3
"""
Provides a function to generate Pascal's Triangle up to n number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows to generate. Must be a non-negative integer.

    Returns:
        list: A list of lists. Each inner list represents a row of the Triangle.
              Returns an empty list if n <= 0.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        return []

    # Start with the first row of Pascal's Triangle
    triangle = [[1]]

    # Build each subsequent row
    for i in range(1, n):
        # Construct the current row using the previous row
        row = [1] + [triangle[i-1][j-1] + triangle[i-1][j]
                     for j in range(1, i)] + [1]
        triangle.append(row)

    return triangle
