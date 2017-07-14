point = 2, 3
x, y = point
date = "October", 5

# Bad practice
xs = 42,
x, = xs
print(x)

# Better
xs = (42, )
[x] = xs
print(xs, x)

person = ("George", "Carlin", "May", 12, 1937)
name, birthday = person[:2], person[2:]
print(name, birthday)

# Named slices
NAME, BIRTHDAY = slice(2), slice(2, None)
print(person[NAME], person[BIRTHDAY])

# Named index
FIRSTNAME = 0
print(person[FIRSTNAME])

# Reverse
print(tuple(reversed((1, 2, 3))))
# The same with slice
print((1, 2, 3)[::-1])

# Bad
print(range(10, -1, -1))
# Better
print(reversed(range(10 + 1)))

# Tuple concatenation
xs, ys = (1, 2), (3, )
print(id(xs) == id(ys))
print(id(xs + ys))
