#!/usr/bin/python3
"""
    pascal traingle
"""
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

traingle_list = []
def pascal_triangle(rows):
    for n in range(rows):
        row_list = []
        for r in range(n + 1):
            nCr = factorial_iterative(n) // (factorial_iterative(n - r) * factorial_iterative(r))
            row_list.append(nCr)
        traingle_list.append(row_list)
    return traingle_list
