"""functools module: partial.
    New function with partial application of the given arguments and keywords.
"""
from functools import partial


f = partial(sorted, key=lambda p: p[1])
print(f([("a", 4), ("b", 2)]))

g = partial(sorted, [2, 3, 1, 4])
print(g())

k = partial(sorted, [("a", 2), ("b", 1)], key=lambda p: p[1])
print(k())
