#!/usr/bin/python3
"""Defines pascal function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal's triangle of n"""

    if n <= 0:
        return ""

    triangle = [[1]]
    for current_row in range(1, n):
        row = [1]
        prev_row = triangle[current_row - 1]
        for el in range(1, current_row):
            row.append(prev_row[el] + prev_row[el - 1])
        row.append(1)
        triangle.append(row)
    return triangle
