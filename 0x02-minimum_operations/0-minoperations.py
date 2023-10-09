#!/usr/bin/python3
'''
This function returns the min num
'''


def minOperations(n):
    '''
    Takes in an int(n) returns an int(n)
    '''
    if n < 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            n //= divisor
            operations += divisor
        divisor += 1
    return operations
