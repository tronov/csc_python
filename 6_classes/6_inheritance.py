class Counter:
    def __init__(self, initial=0):
        self.value = initial


class OtherCounter(Counter):
    def get(self):
        return self.value


c = OtherCounter(42)    # calls Counter.__init__
print(c.get())          # calls OtherCounter.get
print(c.value)          # gets c.__dict__["value"]
