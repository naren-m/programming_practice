# https://leetcode.com/problems/reverse-integer/submissions/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        _2_31 = pow(2, 31)
        INT_MAX = _2_31 - 1
        INT_MIN = -1 * _2_31

        rev = 0
        k = 1
        if x < 0:
            x = abs(x)
            k = -1

        while x > 0:
            rev = rev * 10 + (x % 10)
            x = x // 10

            if INT_MAX < rev or rev <= INT_MIN:
                return 0

        return rev * k


s = Solution()

tests = [
    {'input': 123, 'expected': 321},
    {'input': -123, 'expected': -321},
    {'input': 120, 'expected': 21},
    {'input': pow(2, 31) + 1, 'expected': 0},
    {'input': -2147483412, 'expected': -2143847412},
]

for test in tests:
    rev = s.reverse(test['input'])
    print('Expected {}, got {}'.format(test['expected'], rev))
    assert rev == test['expected']
