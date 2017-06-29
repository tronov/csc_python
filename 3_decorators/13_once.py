"""Decorators usage: @once"""
from functools import wraps


def once(func):

    @wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True

    inner.called = False
    return inner


@once
def initialize_settings():
    print("Settings initialized.")


initialize_settings()
initialize_settings()
initialize_settings()
