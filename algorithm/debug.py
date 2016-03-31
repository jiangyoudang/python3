
def print2_3s(n):
  result = [1]
  i2 = i3 = 0
  for i in range(n):
    _next2, _next3 = result[i2] * 2, result[i3] * 3
    if _next2 > _next3:
      result.append(_next3)
      i3 += 1
    elif _next3 > _next2:
      result.append(_next2)
      i2 += 1
    else:
      result.append(_next2)
      i2 += 1
      i3 += 1
  print(result)
  return result


print2_3s(1)
print2_3s(10)
print2_3s(2)
