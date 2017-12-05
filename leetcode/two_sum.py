# Problem: https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        for i, num in enumerate(nums):
            if num in num_dict:
                return [num_dict[num], i]
            else:
                num_dict[target - num] = i
        return []


s = Solution()

nums = [2, 7, 11, 15]
target = 9

print(s.twoSum(nums, target))

nums = [3, 2, 4]
target = 6

print(s.twoSum(nums, target))

nums = [3, 3]
target = 6

print(s.twoSum(nums, target))
