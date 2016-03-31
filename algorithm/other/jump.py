
inputs = [1, 1, 1, 1, 1, 0, 0, 1, 1, 0]

def reachable(inputs):
  curr_status = [(0,-1)]
  if inputs[0] == 0:
    return False
  options = (-1, 0 , 1)
  visited = set()
  while curr_status:
    next_status = []
    for v,p in curr_status:
      for option in options:
        if v+option <=0:
          continue
        if p+v+option > len(inputs):
          return True
        if 0<= p+v+option < len(inputs) and inputs[p+v+option] == 1:
          # add visited here to avoid repeat
          next_pos = (v+option, p+v+option)
          if next_pos not in visited:
            next_status.append(next_pos)
            visited.add(next_pos)
    print(curr_status)
    curr_status = next_status
  return False


# dp
def reach2(inputs):
  dp = {}
  # stones_pos = [i for i, v in enumerate(inputs) if v == 1]
  if inputs[0] == 0:
    return False
  else:
    dp[0] = {1}
  options = (-1, 0, 1)
  for p in range(0, len(inputs)):
    if inputs[p] == 1:
      if p not in dp:
        return False
      print(p, dp[p])
      for v in dp[p]:
        for dv in options:
          if p + v + dv >= len(inputs):
            return True
          if v+dv > 0:
            dp[p+v+dv] = dp.get(p+v+dv, set())
            dp[p+v+dv].add(v+dv)
  return False




print(reachable(inputs))
print(reach2(inputs))




