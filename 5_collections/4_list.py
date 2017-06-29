l = [0] * 2
print(l)

l = [""] * 2
print(l)

# Values DO NOT copying
chunks = [[0]] * 2
print(chunks)
chunks[0][0] = 42
print(chunks)

# You need to use next notation
chunks = [[0] for _ in range(2)]
chunks[0][0] = 42
print(chunks)

# list methods
xs = [1, 2, 3]
print(xs)
xs.append(42)
print(xs)
# you can extend list with arbitrary sequence
xs.extend({-1, -2})
print(xs)

xs.insert(0, 4)
print(xs)

xs.insert(-1, 42)
print(xs)

xs[1:5] = [0] * 2
print(xs)

# lists concatenation
xs, ys = [1, 2], [3]
print(id(xs) == id(ys), id(xs) == id(xs + ys))

# inplace concatenation
print("\ninplace concatenation:\n" + "=" * 20)
# ~ xs = xs.extend(ys)
xs2 = xs
xs2 += ys
print(id(xs) == id(xs2))

xs = [1, 2, 3]
del xs[:2]
print(xs)

xs = [1, 2, 3]
x = xs.pop(1)
print(xs, x)

print("\nreversing:\n" + "=" * 20)
# reversed, of cause, will return new list
xs = [1, 2, 3]
print(id(list(reversed(xs))) == id(xs))
# but reverse works in place
xs.reverse()
print(xs)

# Same behaviour has method sort
print("\nsorting:\n" + "=" * 20)
xs.sort()
print(xs)

xs.sort(key=lambda x: x % 2, reverse=True)
print(xs)

xs = [(1, 2), (-3, 4)]
xs.sort(key=lambda x: (x[0], -x[1]))
print(xs)

# List is a stack, list is a queue
line = 'List is a stack, list is a queue'
print("\n{}\n".format(line) + "=" * len(line))

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
top = stack.pop()
print(stack, top)

queue = []
queue.append(1)
queue.append(2)
queue.append(3)
first = queue.pop(0)
print(first, queue)
