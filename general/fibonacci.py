# http://www.naren.me/2020-02-15-fibonacci-sequence/
from time import perf_counter as time
from math import sqrt

def fib(n):
    if n <= 1: return n
    k = fib(n-1) + fib(n-2)
    return k


def timed_fib(fib_func, n):
    start = time()
    k = fib_func(n)
    end = time()

    return k, end-start


def fib_dp(n):
    if n in memo: return memo[n]
    if n < 2: return n
    k = fib_dp(n-1) + fib_dp(n-2)
    memo[n] = k
    return k


def fibonacci_formula(n):
    if n < 2: return n
    sq_5 = sqrt(5)
    phi = (1 + sq_5) / 2 # phi = 1.618034
    n = int(((phi ** n) - (1 - phi) ** n) / sq_5 )
    # n = int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

    return n



total_time_formula = 0
total_time_dp = 0
for n in range(1000):
    memo = {}
    fn, t1 = timed_fib(fibonacci_formula, n)
    fn_dp, t2 = timed_fib(fib_dp, n)
    total_time_formula += t1
    total_time_dp += t2
    # print('N:{} formula:{} t_form:{:0.8f}, t_dp{:0.8f}'.format(n, fn, t1, t2))
    print('N:{} t_form:{:0.8f}, t_dp:{:0.8f}'.format(n, t1, t2))

print('Total Time t_form:{:0.8f}, t_dp:{:0.8f}'.format(total_time_formula, total_time_dp))


memo = {}
n = 24
fn, t1 = timed_fib(fibonacci_formula, n)
fn_dp, t2 = timed_fib(fib_dp, n)
print('N:{} t_form:{:0.4f}, t_dp:{:0.4f}'.format(n, t1, t2))