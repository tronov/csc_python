def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    inner.__module__ = func.__module__
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner


@trace
def identity(x):
    """I do nothing useful."""
    return x
