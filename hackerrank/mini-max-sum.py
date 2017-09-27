#!/bin/python3

# Question - https://www.hackerrank.com/challenges/mini-max-sum/problem

import sys


def input():
    return "1 2 3 4 5"


arr = list(map(int, input().strip().split(' ')))

print(sum(arr) - max(arr), sum(arr) - min(arr))
