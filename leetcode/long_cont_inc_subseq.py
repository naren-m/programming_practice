# Problem: https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        position = ans = 0
        for i in range(len(nums)):
            if nums[i - 1] >= nums[i]:
                position = i
            ans = max(ans, i - position + 1)

        return ans


s = Solution()

l = [1, 3, 5, 4, 7]
print(s.findLengthOfLCIS(l))

l = [2, 2, 2, 2, 2]
print(s.findLengthOfLCIS(l))

l = [2]
print(s.findLengthOfLCIS(l))