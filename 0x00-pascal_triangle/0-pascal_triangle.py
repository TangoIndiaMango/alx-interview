#!/usr/bin/python3
from math import factorial

def comb(n, k):
    """
    Calculate the binomial coefficient C(n, k).

    Args:
        n (int): The total number of items.
        k (int): The number of items to choose from the total.

    Returns:
        int: The binomial coefficient C(n, k).
    """
    return int((factorial(n)) / (factorial(k) * factorial(n - k)))
    
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the n-th row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    result = []
    if n <= 0:
        return result
    for count in range(n):
        row = []
        for i in range(count + 1):
            row.append(comb(count, i))
        result.append(row)
    return result
