class Noop:
    __slots__ = ["some_attribute"]

noop = Noop()
noop.some_attribute = 42
print(noop.some_attribute)

noop.other_attribute = 100500

# instances of classes which have __slots__ dict attribute
# require less memory because they haven't __dict__
