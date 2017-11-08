# Problem https://www.hackerrank.com/challenges/ctci-array-left-rotation

from __future__ import print_function


def reverse(a, start, end):
    n = len(a)
    while start < end:
        tmp = a[start]
        a[start] = a[end]
        a[end] = tmp
        start += 1
        end -= 1
    return a


def array_left_rotation(a, n, k):
    a = reverse(a, 0, k - 1)
    a = reverse(a, k, n - 1)
    a = reverse(a, 0, n - 1)
    return a


"""
Input
5 4
1 2 3 4 5
"""

n, k = 5, 4
a = [1, 2, 3, 4, 5]
print(a, n, k)

answer = array_left_rotation(a, n, k)
print(answer)

n, k = 5, 1
a = [1, 2, 3, 4, 5]
print(a, n, k)

answer = array_left_rotation(a, n, k)
print(answer)

n, k = 5, 3
a = [1, 2, 3, 4, 5]
print(a, n, k)

answer = array_left_rotation(a, n, k)
print(answer)