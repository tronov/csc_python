from os import chdir, getcwd


class cd:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved_cwd = getcwd()
        chdir(self.path)

    def __exit__(self, *exc_info):
        chdir(self.saved_cwd)

print(getcwd())

with cd('..'):
    print(getcwd())

print(getcwd())
