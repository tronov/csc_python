# The following code is only for an example, because files in python
# already support context manager

from functools import partial


class opened:
    def __init__(self, path, *args, **kwargs):
        self.opener = partial(open, path, *args, **kwargs)

    def __enter__(self):
        self.handle = self.opener()
        return self.handle

    def __exit__(self, *exc_info):
        self.handle.close()
        del self.handle


with opened(__file__, mode='rt') as handle:
    pass
