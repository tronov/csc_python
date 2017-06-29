"""My implementation of the functools.wraps(), which update inner function props.

    @wraps(func)
    def wrapper(*args, **kwargs):
    ...
    is equivalent to
    def wrapper(*args, **kwargs):
    ...
    wrapper = wraps(func)(wrapper)
"""


def wraps(func):
    def decorator(wrapper):
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__module__ = func.__module__
        return wrapper
    return decorator


def trace(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.__name__ = func.__name__
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper


@trace
def identity(x):
    """I do nothing useful."""
    return x


identity(3)
print(identity.__name__, identity.__doc__)

