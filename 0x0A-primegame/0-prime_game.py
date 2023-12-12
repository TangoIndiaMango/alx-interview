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
    Remove multiples of n in the list ls.
    """
    for i in range(2, len(ls)):
        try:
            ls[n * i] = 0
        except Exception as e:
            break

def isWinner(x, nums):
    """
    x -> num of rounds
    nums -> list of valid integers
    Determines the winner of the game based on prime numbers chosen.
    """

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    numbers = [1 for _ in range(max(nums) + 1)]
    numbers[0], numbers[1] = 0, 0
    for i in range(len(numbers)):
        remove_multiple_prime_numbers(numbers, i)

    for i in nums:
        if sum(numbers[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    else:
        return None
