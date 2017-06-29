class Counter:
    """I count. That is all"""

    all_counters = []               # class attribute

    def __init__(self, initial=0):  # конструктор
        self.value = initial        # запись атрибута экземпляра
        Counter.all_counters.append(self)   # обновление атрибута класса
        # конструктор должен ничего не возвращать

    def increment(self):
        self.value += 1

    def get(self):
        return self.value           # чтение атрибута

# Другой способ объявления атрибута класса. Никогда так не делайте
Counter.other_attribute = 42


class Noop:
    some_attribute = 42
    _internal_attribute = []
    __very_internal_attribute = []  # чтение извне вызовет исключение
    # можно прочесть из Noop._Noop__very_internal_attribute


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

