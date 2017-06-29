"""Decorators usage: @memoized"""
from functools import wraps


def memoized(func):
    cache = {}

    @wraps(func)
    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner


@memoized
def ackermann(m, n):
    if not m:
        return n + 1
    elif not n:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(3, 4))
