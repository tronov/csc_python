"""Using the functools module to update inner function props"""
import functools


def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    functools.update_wrapper(inner, func)
    return inner


@trace
def identity(x):
    """I do nothing useful."""
    return x
