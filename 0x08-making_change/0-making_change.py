#!/usr/bin/python3
"""
Function to determine fewest number
of coins needed to meet a given total
"""


def makeChange(coins, total):
    """
    args: coins -> List of positive integers
          total -> A whole value
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    remaining_total = total

    for coin in coins:
        num_coins = remaining_total // coin

        coin_count += num_coins
        remaining_total -= num_coins * coin
    return coin_count if remaining_total == 0 else -1
