def letter(digits):
  mapping = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
  result = []
  if digits:
    dfs(digits, 0, mapping, [], result)
  return result


def dfs(digits, i, mapping, path, result):
  if i == len(digits):
    result.append(''.join(path))
    return
  chars = mapping[digits[i]]
  for c in chars:
    path.append(c)
    dfs(digits, i + 1, mapping, path, result)
    path.pop()


def letterCombinations(digits):
  """
  :type digits: str
  :rtype: List[str]
  """
  mapping = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
  pre = ['']
  curr = []
  for d in digits:
    curr = []
    chars = mapping[d]
    for c in chars:
      curr.extend([i + c for i in pre])
    pre = curr
  return curr


digits = ''
print(letter(digits))
print(sorted(letter(digits)) == sorted(letterCombinations(digits)))
