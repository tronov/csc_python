class Noop:
    pass


attr = "foo"

noop = Noop()
print("noop has {}attribute {}"
      .format('' if hasattr(noop, attr) else 'not ', attr))
setattr(noop, attr, 'bar')
print(getattr(noop, attr))
