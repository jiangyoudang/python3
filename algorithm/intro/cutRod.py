# -*- coding utf-8 -*-

import sys
import os
import time

l = [0,1,5,8,9,10,17,17,20,24,30]
p = l + [0 for i in range(11,21)]

#bottom up
for i in range(2,21):
    p[i] = max(p[i], max([p[j]+p[i-j] for j in range(1,i//2+1)]))



# for j in range(1,i):
#     p[i] = max(p[i], p[j]+p[i-j])




