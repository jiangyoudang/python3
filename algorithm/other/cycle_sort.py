def cyclesort_simple(l):
  # last_value = 0
  for i in range(len(l)):
    if i != l[i]:
      n = i
      while 1:
        tmp = l[n]
        if n != i:
          l[n] = last_value
        last_value = tmp
        n = last_value
        if n == i:
          l[n] = last_value
          break


def cycle_sort(l):
  for i in range(len(l)):
    if i != l[i]:
      n = l[i]
      while n != i:
        tmp = l[n]
        l[n] = n
        n = tmp
      l[i] = n


def find_cycle(l):
  visited = set()
  cycles = []
  for i in range(len(l)):
    if i != l[i] and i not in visited:
      cycle = [i]
      next_i = l[i]
      while next_i != i:
        cycle.append(next_i)
        next_i = l[next_i]
      cycles.append(cycle)
      visited |= set(cycle)

  return cycles


# l = [1,3,2,0,4,6,5]

l = [4, 0, 5, 1, 6, 2, 7, 3]

# cycle_sort(l)
# cyclesort_simple(l)
print(find_cycle(l))

