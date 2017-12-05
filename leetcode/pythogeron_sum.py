class Solution(object):
    def pythogeronSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        result = list()
        num_dict =  dict()
        for i in range(len(nums)):
            num_dict[abs(nums[i])] = i

        for n in nums:
            n = abs(n)
            if n%2 == 0:
                k = n/2
                k = k*k
                if (k-1) in num_dict and (k+1) in num_dict and k-1 != n and k+1 != n:
                    result.append((k-1, k+1, n))
            if n%2 != 0:
                k = n * n
                k = k//2
                if (k-1) in num_dict and (k+1) in num_dict and k-1 != n and k+1 != n:
                    result.append((k-1, k+1, n))
            

        return result


s = Solution()
l = [3, -63, -13, -5, -3, 4, 7, 12, 16, 65, 1, 2]
print(s.pythogeronSum(l))


