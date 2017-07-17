class Counter:
    def __init__(self, initial=0):
        self.value = initial

    def __repr__(self):
        """Object string representation"""
        return "Counter({})".format(self.value)

    def __str__(self):
        """Human readable format"""
        return "Counted to {}".format(self.value)

print("{!r}".format(Counter(42)))
print("{!s}".format(Counter(42)))
