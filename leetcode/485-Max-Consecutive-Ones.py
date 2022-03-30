# 485. Max Consecutive Ones
# https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes_1(self, nums):
        runningCount = [0] * len(nums)
        i = 0
        for n in nums:
            if n == 1:
                runningCount[i] += 1
            else:
                i +=1 
                
        return max(runningCount)
    
    # One pass solution
    def findMaxConsecutiveOnes(self, nums):
        _max = currentMax = 0
        for n in nums:
            if n == 1:
                # Increment the count of 1's by one.
                _max += 1
            else:
                # Find the maximum till now.
                currentMax = max(_max, currentMax)
                # Reset the count of 1's to zero.
                _max = 0

        #  add the last max
        return max(currentMax, _max)
    
    

tests = [
    {'input': [1, 1, 0, 1, 1, 1], 'expected': 3 },
    {'input': [1,0,1,1,0,1], 'expected': 2 },
    {'input': [0,0,0], 'expected': 0 },
]

s = Solution()

for test in tests:
    n = s.findMaxConsecutiveOnes(test['input'])
    print('Input: {}, Expected {}, got {}'.format(test['input'], test['expected'], n))
    assert n == test['expected']
    
    n = s.findMaxConsecutiveOnes_1(test['input'])
    print('Input: {}, Expected {}, got {}'.format(test['input'], test['expected'], n))
    assert n == test['expected']