class Noop:
    __slots__ = ["some_attribute"]

noop = Noop()
noop.some_attribute = 42
print(noop.some_attribute)

noop.other_attribute = 100500

# экземпляры класса с указанным __slots__ требуют меньше памяти,
# потому что у них отсутствует __dict__
