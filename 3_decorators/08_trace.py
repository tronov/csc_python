"""Decorator with arguments"""

from functools import wraps, update_wrapper
from sys import stderr


def with_arguments(deco):
    @wraps(deco)
    def wrapper(*dargs, **dkwargs):
        def decorator(func):
            result = deco(func, *dargs, **dkwargs)
            update_wrapper(result, func)
            return result
        return decorator
    return wrapper


@with_arguments
def trace(func, handle):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs, file=handle)
        return func(*args, **kwargs)
    return inner


@trace(stderr)
def identity(x):
    """I do nothing useful."""
    return x


identity(3)
print('name: {}, doc: {}'.format(identity.__name__, identity.__doc__))
