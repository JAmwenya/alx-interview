#!/usr/bin/python3
"""
Prime Game: Determine the winner of the most rounds
"""

def sieve_of_eratosthenes(limit):
    """
    Sieve of Eratosthenes: Finds all prime numbers up to 'limit'.
    
    Parameters:
    limit (int): The upper limit of the prime number search.
    
    Returns:
    list: List of primes up to the given 'limit'.
    """
    if limit < 2:
        return []
    
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for num in range(2, int(limit ** 0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """
    Determines the winner of a series of rounds in the Prime Game.
    """
    if x == 0 or not nums:
        return None  # No rounds or empty list of rounds
    
    max_n = max(nums)  # Find the maximum 'n' value
    primes = sieve_of_eratosthenes(max_n)
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n < 2:  # Skip invalid rounds where n < 2
            continue
        
        # Game state initialization
        available_primes = [prime for prime in primes if prime <= n]
        
        # Simulate the game for this round
        current_player = "Maria"  # Maria always starts
        while available_primes:
            # Current player picks the smallest prime
            prime = available_primes.pop(0)
            # Remove this prime and its multiples
            available_primes = [p for p in available_primes if p % prime != 0]
            # Switch to the next player
            current_player = "Ben" if current_player == "Maria" else "Maria"
        
        # Determine winner of the round
        if current_player == "Maria":
            ben_wins += 1  # Maria couldn't make a move, Ben wins
        else:
            maria_wins += 1
    
    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
