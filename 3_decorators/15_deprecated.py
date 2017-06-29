"""Decorators usage: @deprecated"""
from warnings import warn_explicit


def deprecated(func):
    code = func.__code__
    warn_explicit(func.__name__ + ' is deprecated.',
                  category=DeprecationWarning,
                  filename=code.co_filename,
                  lineno=code.co_firstlineno + 1)
    return func


@deprecated
def identity(x):
    return x


print(identity(3))
