"""Decorator with optional arguments"""

from sys import stdout
from functools import wraps


def trace(func=None, *, handle=stdout):
    # for usage with parameters
    if func is None:
        return lambda func: trace(func, handle=handle)

    # for usage without parameters
    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner


@trace
def identity(x):
    """I do nothing useful."""
    return x


identity(3)
print('name: {}, doc: {}'.format(identity.__name__, identity.__doc__))
