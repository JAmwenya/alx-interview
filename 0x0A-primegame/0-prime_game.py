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
    if x <= 0 or not nums:
        return None  # If no rounds or invalid number of rounds
    
    max_n = max(nums)  # Find the maximum 'n' value
    primes = sieve_of_eratosthenes(max_n)  # Precompute all primes
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n < 2:  # Skip invalid rounds where n < 2 (Maria loses automatically)
            ben_wins += 1  # Ben wins as Maria cannot play
            continue
        
        # Game state initialization
        available_numbers = [True] * (n + 1)  # True means available, False means removed
        available_numbers[0] = available_numbers[1] = False  # 0 and 1 are not primes
        
        # Simulate the game for this round
        current_player = "Maria"  # Maria always starts
        while True:
            # Find the smallest available prime number
            prime = None
            for p in primes:
                if p <= n and available_numbers[p]:
                    prime = p
                    break
            
            if prime is None:
                # No available prime number left
                if current_player == "Maria":
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            
            # Remove the prime and its multiples
            for multiple in range(prime, n + 1, prime):
                available_numbers[multiple] = False
            
            # Switch to the next player
            current_player = "Ben" if current_player == "Maria" else "Maria"
    
    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # It's a tie
