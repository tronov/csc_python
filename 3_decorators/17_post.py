"""Decorators usage: @post"""
from functools import wraps
from math import isnan

def post(cond, message):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            assert cond(result), message
            return result
        return inner
    return wrapper


@post(lambda x: not isnan(x), "not a number")
def something_useful():
    return float("nan")


print(something_useful())
