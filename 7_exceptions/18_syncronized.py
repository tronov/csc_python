# The following code is only for an example,
# because most of python sync primitives (including Lock)
# already support context manager
import threading


class syncronized:
    def __init__(self):
        self.lock = threading.Lock()

    def __enter__(self):
        self.lock.acquire()

    def __exit__(self, *exc_info):
        self.lock.release()

with syncronized():
    print("I'm inside syncronized.")
