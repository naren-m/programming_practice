# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanNumerals = {   'I' : 1,
                            'V' : 5,
                            'X' : 10,
                            'L' : 50,
                            'C' : 100,
                            'D' : 500,
                            'M' : 1000 }
        
        prev = s[0]
        num = romanNumerals[prev]
        for n in s[1:]:
            if romanNumerals[prev] < romanNumerals[n]:
                num = romanNumerals[n] - num
            else:
                num += romanNumerals[n]
        
        return num
        


s = Solution()
tests = [
    {'input': "III", 'expected': 3 },
    {'input': "IV", 'expected': 4},
    {'input': "IX", 'expected': 9 },
    {'input': "LVIII", 'expected': 58},
    {'input': "XL", 'expected': 40},
    {'input': "MCMXCIV", 'expected': 1994}
]

for test in tests:
    rev = s.romanToInt(test['input'])
    print('Input {}. Expected {}, got {}'.format(test['input'], test['expected'], rev))
    # assert rev == test['expected']


