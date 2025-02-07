#!/usr/bin/python3
"""
This module contains a function to calculate the minimum number of operations
needed to achieve exactly n characters using Copy All and Paste operations.
"""


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in exactly
    n H characters in the file.

    Parameters:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations, or 0 if n is not possible.
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
