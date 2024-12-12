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
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes
    for num in range(2, int(limit ** 0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]

def isWinner(x, nums):
    """
    Determines the winner of a series of rounds in the Prime Game.
    
    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers representing 'n' for each round.
    
    Returns:
    str: Name of the player with the most wins ("Maria" or "Ben").
    None: If the result is a tie.
    """
    max_n = max(nums)  # Find the maximum 'n' value to compute primes up to this limit
    primes = sieve_of_eratosthenes(max_n)  # Precompute all primes up to max_n
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
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
            maria_wins += 1  # Ben couldn't make a move, Maria wins
    
    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
