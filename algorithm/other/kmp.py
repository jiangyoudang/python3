def preprocess(p):
  T = [0] * len(p)
  cnd = 0
  pos = 2

  T[0] = -1
  T[1] = 0

  while pos < len(p):
    if p[pos - 1] == p[cnd]:
      cnd += 1
      T[pos] = cnd
      pos += 1
    elif cnd > 0:
      cnd = T[cnd]
    else:
      pos += 1
      T[pos] = 0

  return T


def kmp_search(text, T, p):
  m, i = 0, 0
  while m + i < len(text):
    if text[m + i] == p[i]:
      if i == len(p) - 1:
        return m
      i += 1
    elif T[i] > -1:
      m += i - T[i]
      i = T[i]
    else:
      m += 1
      i = 0


patten = 'abcabd'
text = 'abcabcabcabde'

T = preprocess(patten)
print(T)
print(kmp_search(text, T, patten))
