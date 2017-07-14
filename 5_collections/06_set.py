xs, ys, zs = {1, 2}, {2, 3}, {3, 4}
us = set.union(xs, ys, zs)
print(us)
print(xs | ys | zs)

cs = set.intersection(xs, ys, zs)
print(cs)
print(xs & ys & zs)

ds = set.difference(xs, ys, zs)
print(ds)
print(xs - ys - zs)

print(xs.isdisjoint(ys))

# is xs subset ys
print(xs <= ys)

# is xs strict subset ys
print(xs < xs)

# is xs and ys union superset xs
print(xs | ys >= xs)

# set.symmetric_difference(xs, ys)

seen = set()
seen.add(42)
print(seen)

seen.update([1, 2])
print(seen)
seen.update([3], [4, 5], [], [6])
print(seen)

# if 3 not in seen you get error
seen.remove(3)

# try to remove
seen.discard(100500)

# you can not create set of sets,
# because set object has mutable size
# and that is the cause of set object is not hashable
# unhashable = {set(), set()}

# you can use immutable set - frozenset for that purpose
# but you must remember that you can't add or remove element of it
fs = {frozenset(), frozenset()}

