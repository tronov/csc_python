print("{}, {}, how are you?".format("Hello", "Sally"))
print("Today is September, {}th.".format(28))

print("{0}, {1}, {0}".format("hello", "kitty"))
print("{0}, {who}, {0}".format("hello", who="kitty"))

point = 0, 10
print("x = {0[0]}, y = {0[1]}".format(point))

point = {"x": 0, "y": 10}
print("x = {0[x]}, y = {0[y]}".format(point))

# str is 'for human'
print(str("я строка"))
# repr 'for debug'
print(repr("я строка"))
print(ascii("я строка"))

# str (default)
print("{!s}".format("я строка"))
# repr
print("{!r}".format("я строка"))
#asccii
print("{!a}".format("я строка"))

print("{:~^16}".format("foo bar"))
print("int: {0:d} hex: {0:x} oct: {0:o} bin: {0:b}".format(42))
print("{:+08.2f}".format(-42.42))
print("{!r:~^16}".format("foo bar"))
# for more details see documentation
