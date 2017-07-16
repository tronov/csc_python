class Noop:
    some_attribute = 42


noop = Noop()
print(getattr(noop, "some_attribute"))
print(getattr(noop, "some_unexisting_attribute", "surprise!"))
