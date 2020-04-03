# https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1440/
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Base case, if length is 1, return
        if len(s) == 1:
            return s
        a = self.reverseString(s[1:])
        a.append(s[0])
        return a

        

s = Solution()


tests = [
    {'input': ["h","e","l","l","o"], 'expected':  ["o","l","l","e","h"]},
    {'input': ["H","a","n","n","a","h"], 'expected': ["h","a","n","n","a","H"] },
]

for test in tests:
    n = s.reverseString(test['input'])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']