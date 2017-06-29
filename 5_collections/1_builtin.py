t = tuple(), (0, ) * 2
print(t)

s = set()
s.add(1)
s.add(2)
s.add(2)
print(s)

l = list()
l.append(2)
l *= 3
print(l)

d = dict()
d['another'] = 'value'
print('another' in d)
del d['another']
print('another' not in d)
d['key'] = 'value'
d2 = {'key': 'value', 2: 42}
print(d, d2)

print(list(map(len, (t, s, l, d, d2))))
