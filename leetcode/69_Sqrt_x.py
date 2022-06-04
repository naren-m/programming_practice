# https://leetcode.com/problems/sqrtx/
# https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/

class Solution:
    def mySqrt(self, x):
        if x < 2: return x

        l, r = 2, x//2 
        while l <= r:
            m = (l + r) // 2
            sv = m ** 2   
            if x == sv:
                return m
            elif x > sv:
                l = m + 1
            elif x < sv:
                r = m - 1
               
        return r
        

s = Solution()   

tests = [
    {'input': 4, 'expected': 2},
    {'input': 8, 'expected': 2},
    {'input': 9, 'expected': 3},
    {'input': 25, 'expected': 5},
]

for test in tests:
    n = s.mySqrt(test['input'])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']
