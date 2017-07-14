from collections import Counter


class ThreadSafeMixin:
    get_lock = ...

    def increment(self):
        with self.get_lock():
            super().increment()

    def get(self):
        with self.get_lock():
            return super().get()


# Mixin class goes first in the inheritance list
class ThreadSafeCounter(ThreadSafeMixin, Counter):
    @classmethod
    def fromkeys(cls, iterable, v=None):
        pass

