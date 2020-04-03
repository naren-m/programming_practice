# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        u = 0
        for n in nums:
            u = u ^ n
            
        return u

s = Solution()


tests = [
    {'input': [1, 1, 2], 'expected': 2 },
    {'input': [1, 2, 2], 'expected': 1 },
    {'input': [4,1,2,1,2], 'expected': 4 },
]

for test in tests:
    n = s.singleNumber(test['input'])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']