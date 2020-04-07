# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3286/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        # [0,1,0,3,12]
        #  0,1,2,3,4
        end = len(nums) - 1
        while  i < end:
            # j tracks 0
            if nums[i] == 0:
                j = i
            else:
                i += 1
                continue

            while j < end:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j = j + 1

            end -= 1

        return nums

s= Solution()

tests = [
    {'input': [0,1,0,3,12], 'expected':  [1,3,12,0,0]},
    {'input': [0,0,1], 'expected':  [1,0,0]},
]

for test in tests:
    n = s.moveZeroes(test['input'])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']