# binary index tree.


def getSum(BIT, index):
  _sum = 0
  while index > 0 :
    _sum += BIT[index]
    index -= index & -index

  return _sum

def update(BIT, index, val):
  _max = len(BIT)
  _diff = val - BIT[index]
  while index <= _max:
    BIT[index] += _diff
    index += index & -index



