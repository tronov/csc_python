"""Add the flag to switch off the tracer decorator dynamically."""
import functools

trace_enabled = True


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if trace_enabled:
            print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner


@trace
def identity(x):
    """I do nothing useful."""
    return x
