# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not (1 <= len(arr) <= 1000):
            return 0

        d = dict()
        for a in arr:

            try:
                _ = d[a]
            except KeyError:
                d[a] = 1


        count = 0
        for a in arr:
            count += d.get(a+1, 0)

        return count


s= Solution()

tests = [
    {'input': [1,2,3], 'expected':  2},
    {'input': [1,1,3,3,5,5,7,7], 'expected': 0},
    {'input': [1,3,2,3,5,0], 'expected':  3},
    {'input': [1,1,2,2], 'expected':  2},
]

for test in tests:
    n = s.countElements(test['input'])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']