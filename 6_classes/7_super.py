class Counter:
    all_counters = []

    def __init__(self, initial=0):
        self.__class__.all_counters.append(self)
        self.value = initial


class OtherCounter(Counter):
    def __init__(self, initial=0):
        self.initial = initial
        super().__init__(initial)
        # super() returns self.__class__


oc = OtherCounter()
print(vars(oc))
