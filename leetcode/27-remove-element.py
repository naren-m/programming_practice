# https://leetcode.com/problems/remove-element/
# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/

class Solution:
    def removeElement(self, nums, val):
        l = len(nums)
        i = n = 0
        while i < l:
            if nums[i] == val:
                self.leftShift(nums, i)
                n += 1
            else:
                i += 1
                
        return l - n
                
    
    def leftShift(self, nums, index):
        for i in range(index +1, len(nums)):
            nums[i - 1] = nums[i]
        
        nums[-1] = None



tests = [
    {'input': ([3,2,2,3], 3), 'expected': (2, [2,2,None, None])},
    {'input': ([0,1,2,2,3,0,4,2], 2), 'expected': (5, [0,1,3,0,4,None,None,None])},
]

s = Solution()

for test in tests:
    n = s.removeElement(test['input'][0], test['input'][1])
    print('Input: {}, Expected {}, got {}'.format(
        test['input'], test['expected'], n))
    assert n == test['expected'][0]
    for i in range(0, n):
        assert test['input'][0][i] == test['expected'][1][i]
