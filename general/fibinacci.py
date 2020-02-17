from time import perf_counter as time


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
    if n <= 2: return n
    k = fib_dp(n-1) + fib_dp(n-2)
    memo[n] = k
    return k


n= 40
memo = {}
fn, t = timed_fib(fib_dp, n)
print('N({}) Fibonacci number({}) took {:0.3f} seconds'.format(n, fn, t))
