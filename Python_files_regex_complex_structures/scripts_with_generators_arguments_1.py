"""
Write a Python program which takes two digits m (row) and n (column) as arguments(given from command line) and
generates a two dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
"""


def two_domensional_array(m, n):
    for i in range(m):
        for j in range(n):
            yield i*j
        yield '\n'


def print_two_domensional_array(m, n):
    for element in two_domensional_array(m, n):
        if element != '\n':
            print(element, end='   ')
        else:
            print(element, end='')


print_two_domensional_array(5, 6)

