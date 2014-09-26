import collections
current = collections.deque()
current.append(10)
current.append(14)
current.append(3)

print(current.popleft())
print(current)