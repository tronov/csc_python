try:
    b"foo" + "bar"
except TypeError:
    print("We've tried to concat bytes to string.")
