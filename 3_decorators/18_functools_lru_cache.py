"""functools module: lru_cache.
    Least-recently-used cache decorator.
    Saves fixed amount of last calls
"""
from functools import lru_cache


@lru_cache(maxsize=64)
def ackermann(m, n):
    if not m:
        return n + 1
    elif not n:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(3, 4))
print(ackermann.cache_info())
