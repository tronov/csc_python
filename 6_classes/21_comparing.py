# If you want to add abilities of comparison to your class
# you must implement all 6 special ordering methods
class Noop:
    __slots__ = ['value']

    def __init__(self, value=0):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


noop1, noop2 = Noop(1), Noop(2)

print(noop1 == noop2)
print(noop1 != noop2)
print(noop1 < noop2)
print(noop1 <= noop2)
print(noop1 > noop2)
print(noop1 >= noop2)


print('=' * 10)

# There is simplest way to do the same thing
# but it works much slower
# You only need to implement equality comparison method
# and at least one ordering method
from functools import total_ordering


@total_ordering
class Counter:
    __slots__ = ['value']

    def __init__(self, value=0):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

c1, c2 = Counter(1), Counter(2)

print(c1 == c2)
print(c1 != c2)
print(c1 < c2)
print(c1 <= c2)
print(c1 > c2)
print(c1 >= c2)
