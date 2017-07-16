class Noop:
    foobar = 42

    def __getattr__(self, name):
        return name     # identity

print(Noop().foobar)
print(Noop().this_attribute_does_not_declared_in_class_definition)
