# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3287/

class Solution(object):
    def _maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l == 0:
            return 0
        start = prices[0]
        profit = 0
        for i in range(1, l):
            gain = prices[i] - start
            start = prices[i]

            if gain > 0:
                profit += gain

        return profit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start = None
        profit = 0
        for p in prices:
            if start is None:
                start = p
                continue
            gain = p - start
            start = p

            if gain > 0:
                profit += gain

        return profit

s= Solution()

tests = [
    {'input': [7,1,5,3,6,4], 'expected':  7},
    {'input': [1,2,3,4,5], 'expected':  4},
    {'input': [7,6,4,3,1], 'expected':  0},
    {'input': [], 'expected':  0},
]


for test in tests:
    n = s.maxProfit(test['input'])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']