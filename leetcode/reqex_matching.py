# Problem https://leetcode.com/problems/regular-expression-matching/description/


class Solution(object):
    def _match(self, s, p):
        return ((len(s) != 0) and (p[0] == ".") or (s[0] == p[0]))

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        if not self._match(s, p):
            return False
        return self.isMatch(s[1:], p[1:])


tests = [{
    "input": {
        "string": "aa",
        "pattern": "a"
    },
    "expected": False
}, {
    "input": {
        "string": "aa",
        "pattern": "a.."
    },
    "expected": False
}, {
    "input": {
        "string": "aa",
        "pattern": "aa"
    },
    "expected": True
}, {
    "input": {
        "string": "aa",
        "pattern": ".."
    },
    "expected": True
}, {
    "input": {
        "string": "aa",
        "pattern": ".a"
    },
    "expected": True
}, {
    "input": {
        "string": "aa",
        "pattern": "a."
    },
    "expected": True
}]

for t in tests:
    s = Solution()
    res = s.isMatch(t['input']["string"], t['input']["pattern"])
    print(t, res)
    if res != t['expected']:
        print("Test case failed:", res, t['expected'])