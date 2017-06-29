"""Decorators usage: time measurement"""
from functools import wraps
from time import perf_counter


def timethis(func=None, *, n_iter=100):
    if func is None:
        return lambda func: timethis(func, n_iter=n_iter)

    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, end=" ... ")
        acc = float("inf")
        for i in range(n_iter):
            tick = perf_counter()
            result = func(*args, **kwargs)
            acc = min(acc, perf_counter() - tick)
        print(acc)
        return result
    return inner

result = timethis(sum)(range(10**6))
print(result)
