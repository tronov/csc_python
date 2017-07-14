class Counter:
    """I count. That is all"""

    all_counters = []               # class attribute (common for each instance)

    def __init__(self, initial=0):  # an instance initializer method
        self.value = initial        # set the instance attribute
        Counter.all_counters.append(self)   # update the class attribute
        # this method must to return None

    def increment(self):
        self.value += 1

    def get(self):
        return self.value           # get attribute


# The other way to define class attribute. Do not ever do that.
Counter.other_attribute = 42


class Noop:
    some_attribute = 42
    _internal_attribute = []
    __very_internal_attribute = []  # getting that attribute outside the class will throw an Exception
    # you can get in from Noop._Noop__very_internal_attribute


class MemorizingDict(dict):
    from collections import deque
    _history = deque(maxlen=10)

    def set(self, key, value):
        self._history.append(key)
        self[key] = value

    def get_history(self):
        return self._history

d = MemorizingDict({"foo": 42})
d.set("baz", 100500)
print(d.get_history())

d = MemorizingDict()
d.set("boo", 500100)
print(d.get_history())

