# __hash__ has used by dict and set.
# To ensure that your class objects is consistent implement both __hash__ and __eq__
# Use __hash__ only for immutable objects

class Noop:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return len(self.value)

    def __eq__(self, other):
        return self.value == other.value


n1, n2 = Noop('spam'), Noop('spam')
s = set()
s.add(n1)
s.add(n2)
print(len(s))
