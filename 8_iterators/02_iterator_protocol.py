"""An iterator's protocol consists of two methods:
    __iter__ - returns instance of class which implements the protocol of iterator
    __next__ - return the next element of iterator. If it not exists than method
must raise StopIteration exception.

Important, that if __next__ has raised StopIteration exception once,
all following calls of __next__ method also must raised StopIteration exception.

Unlike as in Java, in Python an iterator is also an iterable.
"""


class SimpleIterable:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < 3:
            self.i += 1
            return self.i
        else:
            raise StopIteration


for i in SimpleIterable():
    print(i)


iterator = iter(SimpleIterable())
print(next(iterator))
print(next(iterator))
print(next(iterator, 'There no more items.'))
print(next(iterator, 'There no more items.'))
