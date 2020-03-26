# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if len(s) % 2 != 0: return False
        stack = list()

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            else:
                if len(stack) == 0 or c != stack.pop():
                    return False

        return len(stack) == 0 
        



tests = [
    {'input': "()[]{}", 'expected': True },
    {'input': "()", 'expected': True },
    {'input': "(]", 'expected': False},
    {'input': "([)]", 'expected': False },
    {'input': "(", 'expected': False },
    {'input': "]", 'expected': False },
    {'input': "(((", 'expected': False },
    {'input':  "{[]}", 'expected': True },
]

from time import perf_counter as time
import datetime

s = Solution()
for test in tests:
    start = time()
    result = s.isValid(test['input'])
    end = time()
    
    print('Expected {}, got {}. Time took {} ms'.format(test['expected'], result, datetime.timedelta(end-start).microseconds))
    assert result == test['expected']
