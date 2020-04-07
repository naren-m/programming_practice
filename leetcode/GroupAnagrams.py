# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3288/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = dict()
        for s in strs:
            sortedStr = ''.join(sorted(s))
            try:
                groups[sortedStr].append(s)
            except KeyError:
                groups[sortedStr] = list()
                groups[sortedStr].append(s)

        sol = list()
        for k, v in groups.items():
            sol.append(sorted(v))

        return sol


s= Solution()

tests = [
    {'input': ["eat", "tea", "tan", "ate", "nat", "bat"], 'expected':  [
                                                                        ["ate","eat","tea"],
                                                                        ["nat","tan"],
                                                                        ["bat"]
                                                                        ]},
]

for test in tests:
    n = s.groupAnagrams(test['input'])
    print('Expected {}, got {}'.format(test['expected'], n))
    assert n == test['expected']


