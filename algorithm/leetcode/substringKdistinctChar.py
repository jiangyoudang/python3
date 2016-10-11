
def SubK(s, k):
  if not s or k < 1:
    return 0
  charSet = {}
  left = 0
  chars = 0
  for right, char in enumerate(s):
    if char in charSet:
      charSet[char] += 1
    else:
      if len(charSet) == k:
        while left<right:
          charSet[s[left]] -= 1
          if charSet[s[left]] == 0:
            del charSet[s[left]]
          left += 1
          if len(charSet) < k:
            break

      charSet[char] = 1


    chars = max(chars, right-left+1)
  return chars

s  = 'tetstt'
k = 3
print(SubK(s, k))
