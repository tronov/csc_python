import dis


dis.dis('for x in xs: do_something(name)')

# In python an `for' operator works with any sequence.

# The `GET_ITER' instruction calls `__iter__' method
# of `for' operator argument. This method returns an iterator.

# The `FOR_ITER' instruction calls iterator's `__next__' method
# until `StopIterator' exception is raised.
