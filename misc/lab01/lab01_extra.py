from functools import reduce

"""Coding practice for Lab 1."""

# While Loops

def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"

    nums = [x for x in range(1, n+1) if not(n%x)]
    nums.sort()
    return nums


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"

    return reduce(lambda acc, val: acc * val, range(n-k+1, n+1), 1)
