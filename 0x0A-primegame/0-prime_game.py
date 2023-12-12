#!/usr/bin/python3
"""
This function determines a winner
from two people who take turns in
choosing a prime number
"""

def remove_multiple_prime_numbers(ls, n):
    """
    ls -> a list of numbers
    n -> valid integer
    """
    for i in range(2, len(ls)):
        try:
            ls[n * i] = 0
        except (ValueError, IndexError):
            break

def isWinner(x, nums):
    """
    x -> num of rounds
    nums -> list of valid integers
    """

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    numbers = [1 for i in range(sorted(nums)[-1] + 1)]
    numbers[0], numbers[1] = 0, 0
    for i in range(len(numbers)):
        remove_multiple_prime_numbers(numbers, i)

    for i in nums:
        if sum(numbers[0:i+1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    else:
        return None
