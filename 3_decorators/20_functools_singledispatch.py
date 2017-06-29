"""functools.singledispatch
    Single-dispatch generic function decorator.
"""
from functools import singledispatch


@singledispatch
def pack(obj):
    type_name = type(obj).__name__
    assert False, "Unsupported type: " + type_name


@pack.register(int)
def _(obj):
    return b"I" + hex(obj).encode("ascii")


@pack.register(list)
def _(obj):
    return b"L" + b",".join(map(pack, obj))

print(pack([1, 2, 3]))
print(pack(42))
print(pack(42.0))
