#!/usr/bin/python3
"""
UTF-8 Validation
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes
    :return: True if data is valid UTF-8 encoding, False otherwise
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the most significant bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get only the least significant 8 bits of the number
        byte = num & 0xFF

        if n_bytes == 0:
            # Check how many leading 1's in the byte
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            # If no leading 1's, it is a single-byte character
            if n_bytes == 0:
                continue

            # If the number of bytes is invalid (not 2, 3, or 4), return False
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check that the current byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes to process
        n_bytes -= 1

    # If n_bytes is not zero, there are incomplete characters
    return n_bytes == 0
