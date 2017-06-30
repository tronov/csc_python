

class Path:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return "Path({})".format(self.current)

    # getter property
    @property
    def parent(self):
        return Path(dirname(self.current))


class BigDataModel:
    def __init__(self):
        self._params = []

    @property
    def params(self):
        return self._params

    @property.setter
    def params(self, new_params):
        assert all(map(lambda p: p > 0, new_params))
        self._params = new_params

    @params.deleter
    def params(self):
        del self._params

model = BigDataModel()
model.params = [0.1, 0.5, 0.4]
print(model.params)
