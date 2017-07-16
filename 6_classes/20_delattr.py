class Noop:
    pass


attr = "foo"

noop = Noop()
print("noop has {}attribute {}"
      .format('' if hasattr(noop, attr) else 'not ', attr))
setattr(noop, attr, 'bar')
print("the value of noop.{} is {}".format(attr, getattr(noop, attr)))
delattr(noop, attr)
print("noop has {}attribute {}"
      .format('' if hasattr(noop, attr) else 'not ', attr))
