class Noop:
    """I do nothing at all."""
    pass


print(Noop.__doc__)         # документация класса
print(Noop.__name__)        # имя класса
print(Noop.__module__)      # имя модуля класса
print(Noop.__bases__)       # кортеж имен базовых классов

noop = Noop()
print(noop.__class__)       #
print(noop.__dict__)        # словарь атрибутов объекта (есть у любого объекта)

noop.__dict__["some_other_attribute"] = 100500
print(noop.__dict__)         # словарь атрибутов объекта
print(vars(noop))           # словарь атрибутов объекта
print(noop.some_other_attribute)

del noop.some_other_attribute
