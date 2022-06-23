# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/949/

class Solution:
    def findMin(self, nums) -> int:
        n = len(nums) - 1
        def find_rotate_index(l, r):
            if nums[l] < nums[r]:
                return 0
            while l <= r:
                m = (l+r) // 2
                
                if nums[m] > nums[m+1]:
                    return m+1
                
                if nums[m] < nums[l]: # search right
                    r = m - 1
                else:
                    l = m + 1
  
        if n == 0: return nums[0]
        i = find_rotate_index(0, n)

        return nums[i]
    

s = Solution()   

tests = [
    {'input': [-1,0,3,5,9,12], 'expected': -1 },
    {'input': [4,5,6,7,0,1,2], 'expected': 0 },
    {'input': [0], 'expected': 0 },
    {'input': [3, 1], 'expected': 1 },
    {'input': [5,1,3], 'expected': 1 },
    {'input': [4,5,1,2,3], 'expected': 1 },
    {'input': [3,4,5,1,2], 'expected': 1 },
    {'input': [2,3,4,5,1], 'expected': 1 },
]

for test in tests:
    n = s.findMin(test['input'])
    print('Input {}, Expected {}, got {}'.format(test['input'], test['expected'], n))
    assert n == test['expected']