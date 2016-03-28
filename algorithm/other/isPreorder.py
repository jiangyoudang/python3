"""Can a given array represent a preorder BST"""


def isPre(_range):
  global curr
  global array
  if curr == len(array):
    return True
  _min, _max = _range
  root = array[curr]
  if _min < array[curr] < _max:
    curr += 1
    return isPre((_min, root)) or isPre((root, _max))
  return False


def isPre2():
  global array
  """Uses max stack."""
  stack = []
  root = float('-inf')

  for pre in array:
    if pre < root:
      return False
    while stack and pre > stack[-1]:
      root = stack.pop()

    stack.append(pre)
  return True


array = [2, 4, 3]
curr = 0

print(isPre((float('-inf'), float('inf'))))
print(isPre2())