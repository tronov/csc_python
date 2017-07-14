from functools import wraps


def singleton(cls):
    instance = None

    @wraps(cls)
    def inner(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return inner


@singleton
class Noop:
    """"I do nothing at all."""


# All instances of singleton class refer to the same object
print(id(Noop()) == id(Noop()))
