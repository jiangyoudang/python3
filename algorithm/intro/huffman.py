
def edit(s):
  n = len(s)
  if n == 0:
    return 0
  dp = [[0]*n for _ in range(n)]

  for gap in range(n):
    for left in range(n-gap):
      right = left + gap
      if gap == 0:
        dp[left][right] = 0
      elif gap == 1:
        dp[left][right] = 1
      else:
        if s[left] != s[right]:
          dp[left][right] = min(
            dp[left+1][right-1],
            dp[left][right-1],
            dp[left+1][right]
          ) + 1
        else:
          dp[left][right] = min(
            dp[left+1][right-1],
            dp[left][right-1] + 1,
            dp[left+1][right] + 1
          )



  return dp[0][n-1]


print(edit('abcedb'))
print(edit('bcedb'))
print(edit('') == 0)
print(edit('ab') == 1)
print(edit('aba') == 0)
