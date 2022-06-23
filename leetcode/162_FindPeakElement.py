# https://leetcode.com/problems/first-bad-version/
# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/948/

class Solution:
    def findPeakElement(self, nums) -> int:
        n = len(nums) - 1
        l, r = 0, n
        if n == 0: return 0

        while l < r:
            m = (l + r) // 2
                        
            if nums[m] < nums[m + 1]: # Search right
                l = m + 1
            else: # Search left
                r = m
    
        return l


s = Solution()   

tests = [
    {'input': [1,2,1,3,5,6,4], 'expected': 5},
    {'input': [1,2,3,1], 'expected': 2},
    {'input': [1,2], 'expected': 1},
    {'input': [1], 'expected': 0},
    {'input': [3,5,6,4,1,2,1], 'expected': 2},
    {'input': [6,4,1,2,1], 'expected': 0},


]

for test in tests:
    n = s.findPeakElement(test['input'])
    print('Input {}. Expected {}, got {}'.format(test['input'], test['expected'], n))
    assert n == test['expected']