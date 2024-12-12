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
    if x == 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n < 2:
            continue
        available_primes = [prime for prime in primes if prime <= n]
        current_player = "Maria"
        while available_primes:
            prime = available_primes.pop(0)
            available_primes = [p for p in available_primes if p % prime != 0]
            current_player = "Ben" if current_player == "Maria" else "Maria"
        
        if current_player == "Maria":
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
