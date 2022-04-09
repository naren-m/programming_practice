# https://leetcode.com/problems/duplicate-zeros/
# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

# Solution: https://leetcode.com/problems/duplicate-zeros/solution/

# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        l = len(arr)
        while i < l:
            if arr[i] == 0:
                self.rightShift(arr, index=i)
                i += 1
                if i < l: 
                    arr[i] = 0
            
            i += 1
                
    def rightShift(self, arr, index):
        if len(arr) - 1 == index: return
        for i in range(len(arr)-2, index, -1):
            arr[i+1] = arr[i]
                
                


tests = [
    {'input': [1,0,2,3,0,4,5,0], 'expected': [1,0,0,2,3,0,0,4]},
    {'input': [1,2,3], 'expected': [1,2,3]},
    {'input': [1,2,3,0], 'expected': [1,2,3,0]},
    {'input': [0,0,0,0,0,0,0], 'expected': [0,0,0,0,0,0,0]},
]

s = Solution()

for test in tests:
    s.duplicateZeros(test['input'])
    n = test['input']
    print('Input: {}, Expected {}, got {}'.format(
        test['input'], test['expected'], n))
    assert n == test['expected']
