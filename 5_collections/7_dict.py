d = {2: "no", "yes": 42}
print(d)

# only reasonable cause of using dict constructor
# is when you pass string literals as kwargs
d = dict(foo="bar")
print(d)

# shallow copy
cd = dict(d)
d['foo'] = None
print(d, cd)

# you can add items on copy
cd = dict(d, egg='spam')
print(d, cd)

# make dict from keys collection
print(dict.fromkeys(['foo', 'bar', 15]))
print(dict.fromkeys(['bar', 'baz'], 42))
print(dict.fromkeys('abcd', 3))
# be careful, value is not copying
d = dict.fromkeys(['bar', 'baz'], [2])
d['bar'][0] = 42
print(d)

# to avoid problems with that use dict comprehension
print({ch: [] for ch in 'abcd'})

# dict has special views
print('d.keys={d.keys}, d.values={d.values}, d.items={d.items}'.format(d=d))

# of cause you can use common collections instruments
del d['bar']
print(len(d), 'baz' in d)

# if you want to modify dict, iterate over its copy
for k in set(d):
    del d[k]
print(d)

# failsafe getter
print(d.get('bar', "here is no any 'bar'"))

# failsafe setter
print(d.setdefault('baz', '???'))
print(d.setdefault('baz', 42))

d = {}
d.update([('foo', 'bar')], boo=42)
print(d)

print(d.pop('foo'))
d.clear()
print(d)
