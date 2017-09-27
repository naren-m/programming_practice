#!/bin/python3

# Question https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import sys


def input():
    return """4 3 2 1 3"""


def birthdayCakeCandles(n, ar):
    tallest = max(ar)
    count = 0
    for a in ar:
        if a == tallest:
            count = count + 1
    return count


inp = input().strip().split(' ')
n = int(inp[0])
ar = list(map(int, inp[1:]))
result = birthdayCakeCandles(n, ar)
print(result)
