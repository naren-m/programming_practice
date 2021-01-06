# https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/529/week-2/3291/

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def processStr(word):
            out = list()
            for l in word:
                if l != '#':
                    out.append(l)
                else:
                    if out: out.pop()
            return ''.join(out)

        S = processStr(S)
        T = processStr(T)

        print(S, T)

        return S == T


s = Solution()

tests = [
    {'input': {'S': "ab#c", 'T': "ad#c"}, 'expected': True },
    {'input': {'S': "ab#c", 'T': "ad#c"}, 'expected': True },
    {'input': {'S': "ab#c", 'T': "ad#c"}, 'expected': True },
    {'input': {'S': "ab#c", 'T': "ad#c"}, 'expected': True },
]

from time import perf_counter as time
import datetime

for test in tests:
    start = time()
    rev = s.backspaceCompare(**test['input'])
    end = time()

    print('Expected {}, got {}. Time took {} ms'.format(test['expected'], rev, datetime.timedelta(end-start).microseconds))
    assert rev == test['expected']
