class Solution(object):
    def bruteforce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = list()
        for i in range(len(nums)):
            for j in xrange(i + 1, len(nums)):
                val = nums[i] + nums[j]
                if val == target:
                    ans.append(i)
                    ans.append(j)
                    break
            if len(ans) == 2:
                break

        return ans

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()
        # print(nums, target)
        for i, num in enumerate(nums):
            if num in num_dict:
                return [num_dict[num], i]
            else:
                num_dict[target - num] = i
        return []


s = Solution()

nums = [2, 7, 11, 15]
target = 9

print(s.bruteforce(nums, target))
print(s.twoSum(nums, target))

nums = [3, 2, 4]
target = 6

print(s.bruteforce(nums, target))
print(s.twoSum(nums, target))

nums = [3, 3]
target = 6

print(s.bruteforce(nums, target))
print(s.twoSum(nums, target))
