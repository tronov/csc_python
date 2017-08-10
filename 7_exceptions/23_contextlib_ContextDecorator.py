# instead of writing:
# def f():
#     with context():
#         ...
# you can write:
# @context()
# def f():
#     ...

# To do that your context() must inherits the ContextDecorator class
# as mix-in

from contextlib import suppress as _suppress, ContextDecorator


class suppressed(_suppress, ContextDecorator):
    pass


@suppressed(IOError)
def do_something():
    pass

