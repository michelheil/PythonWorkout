import functools


# @functools.lru_cache(10)
def fak(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res
