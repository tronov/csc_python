g = {'a': {'b'}, 'b': {'c'}}
print(g['a'])

# how to add to graph edges ('b', 'a') and ('c', 'a')?
# answer - use defaultdict

from collections import defaultdict
# set is value factory
g = defaultdict(set, **{'a': {'b'}, 'b': {'c'}})
g['c'].add('a')
print(g)
