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
    if n <= 1:
        return 0

    if is_prime(n):
        return n

    min_op = 0
    for i in range(2, n):
        if n % i == 0:
            curr_op = (int(i + (n - i) / i + 1))
            if curr_op < min_op:
                min_op = curr_op

    return curr_op
