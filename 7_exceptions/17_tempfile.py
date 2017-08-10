import tempfile


with tempfile.TemporaryFile() as handle:
    path = handle.name
    print(path)

try:
    open(path)
except FileNotFoundError as e:
    print("File '{}' was deleted.".format(path))
