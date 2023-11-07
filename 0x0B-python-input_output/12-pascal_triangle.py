#!/usr/bin/python3
"""
returns a list of lists of integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []

    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        result = 1
        for i in range(1, k + 1):
            result = result * (n - i + 1) // i
        return result

    triangle = []
    for i in range(n):
        row = [binomial_coefficient(i, j) for j in range(i + 1)]
        triangle.append(row)

    return triangle
