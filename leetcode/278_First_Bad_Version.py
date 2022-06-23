# 278_First_Bad_Version.py
# https://leetcode.com/problems/first-bad-version/
# https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/



# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        
        while l < r:
            m = (l + r) // 2
            
            if isBadVersion(m) and not isBadVersion(m-1):
                return m

            if isBadVersion(m):
                r = m
            else:
                l = m + 1
                
        return l


