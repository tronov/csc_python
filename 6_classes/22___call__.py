class Identity:
    def __call__(self, x):
        return x

identity = Identity()
print(identity(42))


from functools import wraps

class trace:
    def __init__(self, handle):
        self.handle = handle

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs, file=self.handle)
            return func(*args, **kwargs)
        return inner


from sys import stdout


@trace(stdout)
def identity(x):
    return x

identity(42)
