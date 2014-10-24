import collections
current = collections.deque()
current.append(10)
current.append(14)
current.append(3)

print(current.popleft())
print(current)

a = [1,2]
print(a[3:])



d = {'a':'test_a', 'b':'test_b'}

if 'b' in d:
    d['c'] = 'exist_c'

print(d)

a = b = c = 1
l = []
l[0:0] = [3]

print(l)
b = 2
if 1 < b < 3:
    print(a, b, c )