class Noop:
    """I do nothing at all."""
    pass


print(Noop.__doc__)         # the class documentation
print(Noop.__name__)        # the class name
print(Noop.__module__)      # the class module name
print(Noop.__bases__)       # the tuple of base classes names

noop = Noop()
print(noop.__class__)       #
print(noop.__dict__)        # the object attributes dictionary (almost each object has it)

noop.__dict__["some_other_attribute"] = 100500
print(noop.__dict__)        # the object attributes dictionary
print(vars(noop))           # the same thing
print(noop.some_other_attribute)

del noop.some_other_attribute
