from contextlib import suppress
from os import remove


with suppress(FileNotFoundError):
    # file example.txt does not exist
    remove('example.txt')
    # but suppress catch FileNotFoundError
