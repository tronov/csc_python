class Foo:
    __slots__ = ('spam', 'egg')


foo = Foo()

try:
    foo.bar = 'bar'
except AttributeError:
    print("you can't add attribute into __slots__")


try:
    object().foobar
except AttributeError:
    print("object hasn't foobar attribute")
