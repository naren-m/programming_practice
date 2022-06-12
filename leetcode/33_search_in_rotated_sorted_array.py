# https://leetcode.com/problems/search-in-rotated-sorted-array/
# https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/

class Solution:
    def search(self, nums, target):
        def find_rotate_index(l, r):
            if nums[l] < nums[r]:
                return 0
            
            while l < r:
                m = (l+r)//2
                if nums[m] > nums[m+1]:
                    return m + 1
                if nums[l] < nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        
        def search(l, r):
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
            
            return -1
        
        n = len(nums) - 1
        if n == 0: 
            return 0 if nums[0] == target else -1

        ri = find_rotate_index(0, n)
        
        if ri == 0: # Array not rotated
            return search(0, n)
        
        if nums[ri] == target: return ri
        
        if target < nums[ri]: return search(0, ri) # Search left
        if target > nums[ri]: return search(ri, n) # search right
                    


s = Solution()   

tests = [
    {'input': ([-1,0,3,5,9,12], 9), 'expected': 4},
    {'input': ([-1,0,3,5,9,12], 2), 'expected': -1 },
    {'input': ([4,5,6,7,0,1,2], 0), 'expected': 4},
    {'input': ([4,5,6,7,0,1,2], 3), 'expected': -1 },
    {'input': ([0], 1), 'expected': -1 },
]

for test in tests:
    n = s.search(test['input'][0], test['input'][1])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']



    