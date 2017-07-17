class Counter:
    def __init__(self, initial=0):
        self.value = initial

    def __bool__(self):
        return bool(self.value)

c = Counter()
if not c:
    print("No counts yet.")
