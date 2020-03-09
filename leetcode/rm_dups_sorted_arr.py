# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end = len(nums)
        i = 0
        for j in range(end):
            if nums[i] != nums[j]:
                i+=1
                nums[i]=nums[j]
        return i + 1



s = Solution()


tests = [
    {'input': [1, 1, 2], 'expected': 2 },
    {'input': [0,0,1,1,1,2,2,3,3,4], 'expected': 5 },
    {'input': [0,1,2,3,4], 'expected': 5 },
    {'input': [0,0,0,1,1,1,1,2,2,2,2,2,2,2,3,3,4], 'expected': 5 },

]

for test in tests:
    n = s.removeDuplicates(test['input'])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']

