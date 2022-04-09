# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums):
        if len(nums) == 1: [nums[0] ** 2]
        
        i, j = 0, len(nums) -1
        from collections import deque
        q = deque()
        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                q.appendleft(nums[i] ** 2)
                i += 1
            else:
                q.appendleft(nums[j] ** 2)
                j -=  1
                
        return list(q)
            

tests = [
    {'input': [-7,-3,2,3,11], 'expected': [4,9,9,49,121]},
    {'input': [-4,-1,0,3,10], 'expected': [0,1,9,16,100]},
    {'input': [-2], 'expected': [4]},
    {'input': [0, 0, 0], 'expected':[0, 0, 0]},
]

s = Solution()

for test in tests:
    n = s.sortedSquares(test['input'])
    print('Input: {}, Expected {}, got {}'.format(
        test['input'], test['expected'], n))
    assert n == test['expected']
