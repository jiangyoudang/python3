# inputs = [1, 20, 6, 4, 5]
inputs = [3, 2, 1]
counts = 0

def _merge(i, j):
  global inputs
  _count = 0
  m = (i+j) >> 1
  temp = []
  p1 = i
  p2 = m+1
  while p1 <= m and p2 <= j:
    if inputs[p1] < inputs[p2]:
      temp.append(inputs[p1])
      p1 += 1
    else:
      temp.append(inputs[p2])
      p2 += 1
      _count += m-p1+1
  while p1 <= m :
    temp.append(inputs[p1])
    p1 += 1

  while p2 <= j:
    temp.append(inputs[p2])
    p2 += 1
  inputs[i:j+1] = temp

  return _count


def inversions(i, j):
  global counts
  if i >= j:
    return
  m = (i + j) >> 1
  inversions(i, m)
  inversions(m+1, j)
  counts += _merge(i, j)


inversions(0, len(inputs)-1)
print(counts)
print(inputs)
