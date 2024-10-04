#!/usr/bin/python3
from math import factorial
"""
    pascal traingle
"""
traingle_list = []
def pascal_triangle(rows):
    for n in range(rows):
        row_list = []
        for r in range(n + 1):
            nCr = factorial(n) // (factorial(n - r) * factorial(r))
            row_list.append(nCr)
        traingle_list.append(row_list)
    return traingle_list
