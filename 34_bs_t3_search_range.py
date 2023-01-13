# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/

class Solution:
    def searchRange(self, nums, target):      
        def binarySearch(nums, l, r, target):
            if len(nums) == 0:
                return -1

            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    return m
                if nums[m] < target: # Search right
                    l = m + 1
                else:
                    r = m - 1
                    
            return -1
            
        
        n = len(nums) - 1
        l, r = 0, n
        
        p = binarySearch(nums, l, r, target)
        if p == -1: 
            return [-1, -1]
        li = ri = p
        
        while True:
            fi = binarySearch(nums, 0, li - 1, target)
            if fi == -1: 
                break
            
            li = fi
        
        while True:
            fi = binarySearch(nums, ri + 1, n, target)
            if fi == -1: 
                break

            ri = fi

        return  [li, ri]

            
tests = [        
    {'input': ([5,7,7,8,8,10], 8), 'expected': [3,4]},
    {'input': ([5,7,7,8,8,8], 8), 'expected': [3,5]},
    {'input': ([8,8,8,8,8,8], 8), 'expected': [0,5]},
    {'input': ([5,7,7,8,8,10], 6), 'expected': [-1,-1]},
    {'input': ([], 0), 'expected': [-1,-1]},
    {'input': ([2,2], 3), 'expected': [-1,-1]},
    {'input': ([2,2], 2), 'expected': [0,1]},
]

s = Solution()   

for test in tests:
    n = s.searchRange(test['input'][0], test['input'][1])
    print('Input: {}, Expected {}, got {}'.format(test['input'], test['expected'], n))
    assert n == test['expected']
