# instead of writing that typically piece of code:
f = open(__file__, 'r')
try:
    f.read()
finally:
    f.close()

# you can write the same shortly:
with open(__file__, 'r') as f:
    f.read()

# If your object has methods __enter__ and __exit__,
# then it is the context manager. And it might be used in 'with' statement.

# __enter__ is called in 'with' statement
# and its return value assigning to the name after 'as' keyword.

# __exit__ is called after execution the body of the 'with' block.
# It takes three arguments: exception type, exception object, exception traceback.
# If the 'with' statement body raises an exception, it passing to the __exit__ method.
# You can suppress raised exception by returning True from the __exit__ method.


with open(__file__, 'r') as f1, open(__file__, 'r') as f2:
    f1.read(), f2.read()

# is equivalent to

with open(__file__, 'r') as f1:
    with open(__file__, 'r') as f2:
        f1.read()
        f2.read()
