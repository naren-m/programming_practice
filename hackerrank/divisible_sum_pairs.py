# Problem https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


def divisibleSumPairs(n, k, ar):
    nums = [0] * k
    count = 0

    for i, num in enumerate(ar):
        modulus = num % k
        count += nums[(k - modulus) % k]
        nums[num % k] += 1

    return count


ar = [1, 3, 2, 6, 1, 2]
k = 3
n = 6

print(divisibleSumPairs(n, k, ar))
