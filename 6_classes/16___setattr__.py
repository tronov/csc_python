class Guarded:
    guarded = []

    def __setattr__(self, name, value):
        assert name not in self.guarded
        super().__setattr__(name, value)


class Noop(Guarded):
    guarded = ["foobar"]

    def __init__(self):
        self.__dict__["foobar"] = 42

noop = Noop()

noop.foo = "foo is ok"
print(noop.foo)
print(noop.foobar)

# Will raise AssertionError
# noop.foobar = 13
# But you still can write the next
noop.__dict__["foobar"] = 27

print(noop.foobar)
