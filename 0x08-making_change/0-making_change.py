#!/usr/bin/python3

def makeChange(coins, total):
    # If total is 0 or less, no coins are needed
    if total <= 0:
        return 0
    
    # Initialize dp array with infinity values. dp[i] will be the minimum number of coins needed for i amount
    dp = [float('inf')] * (total + 1)
    
    # Base case: zero coins needed for amount 0
    dp[0] = 0
    
    # Loop through each coin in the denominations
    for coin in coins:
        for i in range(coin, total + 1):
            # Update dp[i] to the minimum number of coins by considering the current coin
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still infinity, return -1 as it's impossible to make the total
    return dp[total] if dp[total] != float('inf') else -1
