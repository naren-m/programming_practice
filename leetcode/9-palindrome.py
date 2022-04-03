class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True

        if x < 0 or x % 10 == 0:
            return False

        rev = 0

        while x > rev:
            rev = rev * 10 + (x % 10)
            x = x // 10

        return ((rev == x) or (x == rev/10))


s = Solution()
tests = [
    {'input': 121, 'expected': True},
    {'input': -121, 'expected': False},
    {'input': 1221, 'expected': True},
    {'input': 0, 'expected': True},
    {'input': 10, 'expected': False},
    {'input': 100, 'expected': False},
    {'input': pow(2, 31) + 1, 'expected': False},
]

for test in tests:
    rev = s.isPalindrome(test['input'])
    print('Input {}. Expected {}, got {}'.format(
        test['input'], test['expected'], rev))
    assert rev == test['expected']
