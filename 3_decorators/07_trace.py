"""Decorator with argument"""

from functools import wraps
from sys import stderr


def trace(handle):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs, file=handle)
            return func(*args, **kwargs)
        return inner
    return decorator


@trace(stderr)
def identity(x):
    """I do nothing useful."""
    return x
