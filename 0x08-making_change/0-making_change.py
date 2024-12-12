#!/usr/bin/python3
"""
module that calculates minimum number of coins required to make a given total.

Functions:
    make_change(coins: list, total: int) -> int
        Calculates the minimum number of coins needed to make a given total.
"""

def make_change(coins, total):
    """
    Calculate the minimum number of coins required to achieve the given total.

    Parameters:
        coins (list of int): A list of coin denominations.
        total (int): The total amount to be achieved.

    Returns:
        int: The minimum number of coins needed to make up the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if it's impossible to make the total.

    Example:
        >>> make_change([1, 2, 5], 11)
        3
        >>> make_change([2], 3)
        -1
    """
    # Check for invalid coin list
    if not coins:
        return -1

    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0

    # Initialize dp array with infinity values. dp[i]=minimum number of coins
    dp = [float('inf')] * (total + 1)

    # Base case: zero coins needed for amount 0
    dp[0] = 0

    # Loop through each coin in the denominations
    for coin in coins:
        for i in range(coin, total + 1):
            # Update dp[i] to the minimum number of coins
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, return -1
    return dp[total] if dp[total] != float('inf') else -1
