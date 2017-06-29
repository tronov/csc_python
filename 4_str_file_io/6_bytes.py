# bytes related with string by methods encode() and decode()

byte = b"\00\42\24\00"
print(byte)

byte = rb"\00\42\24\00"
print(byte)

chunk = "я строка".encode("utf-8")
print(chunk)
print(chunk.decode("utf-8"))

chunk = "я строка".encode("cp1251")
print(chunk.decode("utf-8", "replace"))

import sys
print(sys.getdefaultencoding())
