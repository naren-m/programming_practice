# https://leetcode.com/problems/longest-common-prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) == 0: return prefix
        if len(strs) == 1: return strs[0]
        shortest = min(strs, key=len)
        for i, c in enumerate(shortest):
            same = False
            for s in strs:
                try:
                    if c == s[i]:
                        same = True
                    else:
                        same = False
                        break
                except IndexError:
                    same = False
                    break
                
            if same:
                prefix += c
            else:
                break
            
        
        return prefix

    def betterLongestCommonPrefix(self, strs):
        # https://leetcode.com/problems/longest-common-prefix/discuss/6918/Short-Python-Solution
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]

        return shortest


s = Solution()





tests = [
    {'input': ["flower","flow","flight"], 'expected': "fl" },
    {'input': ["abc", "cba"], 'expected': "" },
    {'input': ["aca","cba"], 'expected': "" },
    {'input': ["a"], 'expected': "a" },
]

from time import perf_counter as time
import datetime

for test in tests:
    start = time()
    # rev = s.longestCommonPrefix(test['input'])
    rev = s.betterLongestCommonPrefix(test['input'])
    end = time()
    
    print('Expected {}, got {}. Time took {} ms'.format(test['expected'], rev, datetime.timedelta(end-start).microseconds))
    assert rev == test['expected']
