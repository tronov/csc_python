# KeyError and IndexError inherited from LookupError base class

try:
    {}['foobar']
except KeyError:
    print("empty dict hasn't 'foobar' key")


try:
    [][0]
except IndexError:
    print("empty list hasn't an element at index 0")
