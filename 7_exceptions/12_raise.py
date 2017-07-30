try:
    raise TypeError
except TypeError:
    print("TypeError has occurred!")


try:
    raise TypeError("type mismatch")
except TypeError as e:
    print("TypeError with args '{}' has occurred!".format(e.args))


try:
    raise TypeError
except Exception as e:
    if isinstance(e, TypeError):
        try:
            raise       # will raise last cached exception
        except TypeError:
            print("That TypeException was catched, but raised again")


try:
    {}['foobar']
except KeyError as e:
    try:
        raise RuntimeError('Ooops!') from e
    except Exception as e1:
        print(e1.__cause__, ' '.join(e.args))
