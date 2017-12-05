class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        num_dict = dict()
        for i in range(len(nums)):



s = Solution()

nums = [2, 7, 15, 11]
target = 20

s.threeSum(nums)
