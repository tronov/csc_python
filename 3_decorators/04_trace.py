"""Wrapping the function with @functools.wraps(func) decorator"""
import functools


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner


@trace
def identity(x):
    """I do nothing useful."""
    return x
