# https://projecteuler.net/problem=3


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in range(30):
    print(i, is_prime(i))

def prime_num(max_num=0):
    for i in range(max_num):
        if 


