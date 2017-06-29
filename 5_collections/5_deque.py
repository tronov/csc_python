from collections import deque

q = deque()
print(q)

q = deque([1, 2, 3])
q.appendleft(0)
print(q)

q.append(4)
print(q)

q.popleft()
print(q)

q = deque([1, 2], maxlen=2)
q.append(0)
q.append(1)
q.append(2)
print(q)
