class Noop:
    pass


noop = Noop()
print(hasattr(noop, 'foo'))
noop.foo = "bar"
print(hasattr(noop, 'foo'))
noop.__delattr__('foo')
print(hasattr(noop, 'foo'))
