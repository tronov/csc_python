class Counter:
    def __init__(self, initial=0):
        self.value = initial

    def __format__(self, format_spec):
        return self.value.__format__(format_spec)


c = Counter(42)
print("Counted to {:b}".format(c))
