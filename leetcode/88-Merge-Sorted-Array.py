# https://leetcode.com/problems/merge-sorted-array/
# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

# Solution: https://leetcode.com/problems/merge-sorted-array/solution/

# Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
#   representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
#   and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge_solution(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        
        for p in range(m + n -1, -1, -1):
            if p2 < 0:
                break
            
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
    
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = k = 0
        while j < m + n and k < n:
            if nums1[j] > nums2[k]:
                self.rightShift(nums1, j)
                nums1[j] = nums2[k]
                k += 1
            j += 1

        j = m + k

        while k < n and j < m+n:
            nums1[j] = nums2[k]
            k += 1
            j += 1

    def rightShift(self, arr, index):
        i = len(arr) - 2
        while i >=index:
            arr[i+1] = arr[i]
            i -= 1
                
        
        
tests = [
    {'input': ([1,2,3,0,0,0], 3, [2,5,6], 3), 'expected': [1,2,2,3,5,6]},
    {'input': ([4,5,6,0,0,0], 3, [1,2,3], 3), 'expected': [1,2,3,4,5,6]},
    {'input': ([4,0,0,0,0,0], 1, [1,2,3,5,6], 5), 'expected': [1,2,3,4,5,6]},
    {'input': ([1, 0], 1, [2], 1), 'expected': [1, 2]},
    {'input': ([1], 1, [], 0), 'expected': [1]},
    {'input': ([0], 0, [1], 1), 'expected': [1]},
]

s = Solution()

for test in tests:
    i = test['input']
    actual = [x for x in i[0]]
    s.merge(nums1=i[0], m=i[1], nums2=i[2], n=i[3])
    expected = i[0]
    print('Input: {}, {}, Expected {}, got {}'.format(
        actual, i[2] , test['expected'], expected))
    assert expected == test['expected']

tests = [
    {'input': ([1,2,3,0,0,0], 3, [2,5,6], 3), 'expected': [1,2,2,3,5,6]},
    {'input': ([4,5,6,0,0,0], 3, [1,2,3], 3), 'expected': [1,2,3,4,5,6]},
    {'input': ([4,0,0,0,0,0], 1, [1,2,3,5,6], 5), 'expected': [1,2,3,4,5,6]},
    {'input': ([1, 0], 1, [2], 1), 'expected': [1, 2]},
    {'input': ([1], 1, [], 0), 'expected': [1]},
    {'input': ([0], 0, [1], 1), 'expected': [1]},
]

for test in tests:
    i = test['input']
    actual = [x for x in i[0]]
    s.merge_solution(nums1=i[0], m=i[1], nums2=i[2], n=i[3])
    expected = i[0]
    print('Input: {}, {}, Expected {}, got {}'.format(
        actual, i[2] , test['expected'], expected))
    assert expected == test['expected']