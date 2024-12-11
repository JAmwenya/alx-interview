#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate. Must be a positive integer.

    Returns:
        list: A list of lists, where each inner list represents a row of Pascal's Triangle.
              Returns an empty list if n <= 0 or if a TypeError occurs.

    Raises:
        TypeError: If n is not an integer.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    try:
        # Initialize the triangle structure
        triangle = []

        # Check if n is an integer
        if not isinstance(n, int):
            raise TypeError("n must be an integer")

        # Return an empty list for non-positive values of n
        if n <= 0:
            return []

        # Start with the first row of Pascal's Triangle
        triangle = [[1]]

        # Build each subsequent row
        for i in range(1, n):
            # Construct the current row using the previous row
            row = [1] + [triangle[i-1][j-1] + triangle[i-1][j] for j in range(1, i)] + [1]
            triangle.append(row)

        return triangle

    except TypeError as e:
        # Handle cases where n is not an integer
        print(e)
        return []

    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []
