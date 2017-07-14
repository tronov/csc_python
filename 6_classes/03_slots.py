class Noop:
    __slots__ = ["some_attribute"]  # that is magic attribute which defines the class attributes dict

noop = Noop()
noop.some_attribute = 42
print(noop.some_attribute)

noop.other_attribute = 100500

# you can't set attribute which is not defined in __slots__

# yet another way to get the class attribute
print(Noop.some_attribute.__get__(noop))

# instances of classes which have __slots__ dict attribute
# require less memory because they haven't __dict__

# Usually you should use namedtuple instead of class with __slots__
