# https://projecteuler.net/problem=3

import math

def sqrt(n):
    return int(math.sqrt(n))

def prime_factors(n):
    pf = set()
    while n %2 == 0:
        n = n // 2
        pf.add(2)

    factor = 3
    max_factor = sqrt(n)
    
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            pf.add(factor)
            while n % factor == 0:
                n = n // factor 
            max_factor = sqrt(n)
        factor += 1

    if n != 1:
        pf.add(n)
    
    return pf

pfs = prime_factors(600851475143)
print(pfs)
print(max(pfs))
