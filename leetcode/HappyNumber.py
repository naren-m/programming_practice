# HappyNumber.py
# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3284/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = list()
        while True:
            n = sumOfSquares(n)
            if n in seen:
                break
            seen.append(n)

        return n == 1

def sumOfSquares(n):
    sqSum = 0
    while n > 0:
        k = n % 10
        n = n // 10
        sqSum += k * k
    return sqSum


def happyNum(n):
    seen = list()
    while n not in [0, 1, 4, 16, 20, 37, 42, 58, 89, 145]:
        n = sumOfSquares(n)
        seen.append(n)
        print(n)

    print(n)

def _happyNum(n):
    seen = list()
    while True:
        n = sumOfSquares(n)
        if n in seen:
            break
    
        seen.append(n)

    return n == 1

s= Solution()

tests = [
    {'input': 19, 'expected': True},
    {'input': 123, 'expected': False },
    {'input': 94, 'expected': True },
]

for test in tests:
    n = s.isHappy(test['input'])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']