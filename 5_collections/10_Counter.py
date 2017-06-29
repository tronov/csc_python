# Counter is multiset, which counts values of any hashable collection

from collections import Counter
c = Counter(['foo', 'foo', 'foo', 'bar'])
c['foo'] += 1
print(c)

# Counter supports all dict methods and add some new
print(c.pop('foo'))
# accessing for non existing key did nor raising an exception
print(c['boo'])

# elements() returns iterable
print(list(c.elements()))

# most_common(n) returns n most common elements
print(list(c.most_common(1)))

# update() and subtract() updates counter by elements
c.update(['bar'])
print(c)
c.subtract({'foo': 2})
print(c)


c1 = Counter(foo=4, bar=-1)
c2 = Counter(foo=2, bar=2)
# c1[k] + c2[k]
print(c1 + c2)
# c1[k] - c2[k]
print(c1 - c2)
# min(c1[k], c2[k])
print(c1 & c2)
# max(c1[k], c2[k])
print(c1 | c2)
# Note: binary operations return only keys with positive frequencies

