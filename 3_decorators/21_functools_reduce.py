"""functools.reduce
    Apply a function of two arguments cumulatively to the items of a sequence.
"""
from functools import reduce


result = reduce(lambda acc, d: 10 * acc + int(d), "1914", 0)
print(result)
