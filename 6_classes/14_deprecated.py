import warnings
from functools import wraps


def deprecated(cls):
    orig_init = cls.__init__

    @wraps(cls.__init__)
    def new_init(self, *args, **kwargs):
        warnings.warn(cls.__name__ + " is deprecated.", category=DeprecationWarning)
        orig_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls


@deprecated
class Counter:
    def __init__(self, initial=0):
        self.value = initial


# DeprecationWarning is suppressed by default. Let's turn it on.
warnings.simplefilter("always")

c = Counter()
