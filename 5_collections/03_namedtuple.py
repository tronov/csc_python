from collections import namedtuple


Person = namedtuple("Person", ["name", "age"])
p = Person("George", age=77)
print(p._fields)
print(p.name, p.age)

# named tuple behaves like ordinary tuple
print(p + (1, 3))

# As OrderedDict
print(p._asdict())

p2 = p._replace(name="Bill")
print(p2)
