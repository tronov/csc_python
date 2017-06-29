"""Decorators usage: @pre"""
from functools import wraps
from math import log

def pre(cond, message):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            assert cond(*args, **kwargs), message
            return func(*args, **kwargs)
        return inner
    return wrapper


@pre(lambda x: x > 0, "negative argument")
def checked_log(x):
    return log(x)


print(checked_log(42))
print(checked_log(-42))
