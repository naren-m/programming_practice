# https://leetcode.com/problems/find-numbers-with-even-number-of-digits
# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/


from unicodedata import digit


class Solution:
    # Find numbers with even number of digits
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for n in nums:
            digits = 0
            while n > 0:
                n //= 10
                digits += 1
            if digits != 0 and digits % 2 == 0:
                count += 1
        return count


tests = [
    {'input': [12, 345, 2, 6, 7896], 'expected': 2},
    {'input': [555, 901, 482, 1771], 'expected': 1},
    {'input': [0, 0, 0], 'expected': 0},
]

s = Solution()

for test in tests:
    n = s.findNumbers(test['input'])
    print('Input: {}, Expected {}, got {}'.format(
        test['input'], test['expected'], n))
    assert n == test['expected']
