# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/


class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums)
        
        return self.binarySearch(l, r, nums, target)
    
    def binarySearch(self, l, r, nums, target):
        m = (l + r)/2
        
        if m > r or m < l:
            return -1

        if nums[m] == target:
            return m
        
        if target < nums[m]:
            r = m
        elif target > nums[m]:
            l = m

        return self.binarySearch(l, r, nums, target)
        

tests = [
    {'input': ([-1,0,3,5,9,12], 9), 'expected': 4},
    {'input': ([-1,0,3,5,9,12], 2), 'expected': -1},
]

s = Solution()

for test in tests:
    n = s.search(test['input'][0], test['input'][1])
    print('Input: {}, Expected {}, got {}'.format(
                test['input'], test['expected'], n))
    assert n == test['expected']
