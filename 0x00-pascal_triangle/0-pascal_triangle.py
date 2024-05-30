#!/usr/bin/python3
"""Pascal Triangle Implementation"""


def pascal_triangle(n):
    """Pascal Triangle Implementation"""
    pascal = []

    if n >= 1:
        pascal = [[1]]
  
    if n >= 2:
        i = 1
        for i in range(i, n):
            temp = []
            m = i + 1

            temp.append(1)
            for j in range(1, m - 1):
                temp.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            temp.append(1)
            pascal.append(temp)

    return pascal
