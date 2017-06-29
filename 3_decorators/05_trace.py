"""Add the flag to switch off the tracer decorator at the compile time."""
import functools

trace_enabled = True


def trace(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner if trace_enabled else func


@trace
def identity(x):
    """I do nothing useful."""
    return x
