#!/usr/bin/python3
"""
    pascal traingle
"""


def pascal_triangle(rows):
    """
        Returns a list of integers
        representing the Pascal Triangle of n
        returns empty list if n <= 0
    """
    traingle_list = []
    for n in range(rows):
        row_list = []
        nCr = 1
        for r in range(n + 1):
            if r > 0:
                nCr = nCr * (n - r + 1) // r
            row_list.append(nCr)
        traingle_list.append(row_list)
    return traingle_list
