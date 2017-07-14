import sys

# read unicode text from sys.stdin
name = input("Name: ")

# write unicode text to sys.stdout and sys.stderr
print(name)
print(name, file=sys.stdout)
print("No errors", file=sys.stderr)

print(*range(4))
print(*range(4), sep="_")
print(*range(4), end="\n--\n")

# you can flush output with print
# print("text", file=file, flush=True)

import io
handle = io.StringIO("foo\n\bar")
print(handle.readline())
handle.write("barracuda")
print(handle.getvalue())

# also exists io.BytesIO(b"foobar")
