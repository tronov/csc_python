try:
    b"foo" + "bar"
except TypeError:
    print("We've tried to concat bytes to string.")

# see more at https://docs.python.org/3/library/exceptions.html
