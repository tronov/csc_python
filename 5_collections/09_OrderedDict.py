d = dict([('foo', 'bar'), ('boo', 42)])
print(list(d))

# OrderedDict saves key order
from collections import OrderedDict
d = OrderedDict([('foo', 'bar'), ('boo', 42)])
print(list(d))

d['foo'] = '???'
d['bar'] = '???'
print(list(d))
