# https://leetcode.com/problems/binary-search/
# https://leetcode.com/explore/learn/card/binary-search/138/background/1038/



class Solution:
    def search(self, nums, target):
        return self.binarySearch(0, len(nums), nums, target)
    
    def binarySearch(self, l, r, nums, target):
        if l >= r:
            return -1
        
        m = (l + r) // 2

        if target == nums[m]:
            return m
        if target < nums[m]:
            r = m
        else:
            l = m + 1
            
        return self.binarySearch(l, r, nums, target)
        
            
        
s = Solution()   

tests = [
    {'input': ([-1,0,3,5,9,12], 9), 'expected': 4},
    {'input': ([-1,0,3,5,9,12], 2), 'expected': -1 },
]

for test in tests:
    n = s.search(test['input'][0], test['input'][1])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']