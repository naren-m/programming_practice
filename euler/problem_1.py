# URL: https://projecteuler.net/problem=1


def sum_of_natural_numbers(n):
    return int(n * ((n+1)/2))

def sum_of_multiples(n, k):
    _n = n//k
    return k * sum_of_natural_numbers(_n)


sol = sum_of_multiples(999, 3) + sum_of_multiples(999, 5) - sum_of_multiples(999, 15)
print(sol)