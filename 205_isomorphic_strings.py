# https://leetcode.com/problems/isomorphic-strings/

class Solution:

    def isIsomorphic(self, s, t):
        if len(s) != len(t): return False

        sd = dict()
        td = dict()

        for i in range(len(s)):
            sd[s[i]] = i
            td[t[i]] = i

        for i in range(len(s)):
            if sd[s[i]] != td[t[i]]:
                return False

        
        return True


        
s = Solution()   

tests = [
    {'input': ("add", "egg"), 'expected': True},
    {'input': ("paper", "tutle"), 'expected': True},
    {'input': ("car", "bar"), 'expected': True },
    {'input': ("foo", "bar"), 'expected': False },
    {'input': ("bbbaaaba", "aaabbbba"), 'expected': False}
]

for test in tests:
    n = s.isIsomorphic(test['input'][0], test['input'][1])
    print('Input: {}, Expected {}, got {}'.format(test['input'], test['expected'], n))
    assert n == test['expected']