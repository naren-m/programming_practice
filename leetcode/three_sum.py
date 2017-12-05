# Problem: https://leetcode.com/problems/3sum/description/


class Solution(object):
    def threeSum_(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        num_dict = dict()
        result = list()
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(1, len(nums)):
                val = -1 * (nums[i] + nums[j])
                if val in num_dict:
                    if num_dict[val][0] + num_dict[val][1] + nums[j] == target:
                        result.append([nums[j]] + num_dict[val])
                else:
                    num_dict[val] = [nums[i], nums[j]]

        return result

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        result = list()
        nums.sort()
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    result.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return result


s = Solution()
l = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(l))
