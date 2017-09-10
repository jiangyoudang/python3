import numpy as np

A = [
    [1,2],
    [3,2]
]

B = [
    [1,0],
    [4,4]
]

data1 = np.array(A)
data2 = np.array(B)

ans1 = data1 * data2
ans = np.dot(data1, data2)

print(ans)
print(ans1)
sort1 = ans.sort()
print(sort1)
