#!/usr/bin/python3
"""
Copy all || Paste >> Those are the only allowed operations to use.
write a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def is_prime(n):
    """
    Check if it's prime number or not
    """
    not_prime = False
    for i in range(2, n):
        if n % i == 0:
            not_prime = True

    if not_prime:
        return False
    else:
        return True


def minOperations(n):
    """
    # if prime number return n
    # loop from i=2 to n and divide n by i
    # if mod == 0:
    # min = base + (n - base) / base + 1
    """
    if is_prime(n) or n == 1:
        return n

    all_ops = []
    for i in range(2, n):
        if n % i == 0:
            all_ops.append(int(i + (n - i) / i + 1))

    return min(all_ops)
