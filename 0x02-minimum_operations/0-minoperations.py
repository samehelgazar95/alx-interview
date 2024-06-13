#!/usr/bin/python3
"""
Copy all || Paste >> Those are the only allowed operations to use.
write a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.

MY CODE DIDNOT PASS FOR 3 CASES, THE LOWER ONE PASSES FOR ALL CASES (NOT MINE)
The underlying principle behind solving this problem is
to find the largest divisor of the current (n) and then
update (n) by dividing it by this largest divisor.
This process aims to minimize the number of operations needed to
construct exactly (n) H characters by systematically reducing (n)
through division by its largest possible factors.
"""


# def minOperations(n):
#     """
#     # loop from i=2 to n and divide n by i
#     # if mod == 0:
#     # min = base + (n - base) / base + 1
#     """
#     if n <= 1:
#         return 0

#     min_op = 0
#     for i in range(2, n):
#         if n % i == 0:
#             curr_op = (int(i + ((n - i) / i) + 1))
#             if curr_op < min_op:
#                 min_op = curr_op

#     return curr_op

def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return ops
