__author__ = 'congliu'

import urllib.request
import re
import pickle
import time
# 4


#url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
#nothing = '12345'
#txt_w = open('4.txt','w')
#for i in range(400):
#    f = urllib.request.urlopen(url+''.join(nothing))
#    content = f.read().decode('utf-8')
#
#    nothing = re.findall(r'[0-9]+',content)
#    #print(type((f.read().decode('utf-8'))))
#    txt_w.write(content+'\n')


#  5

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
f2 = open('5.txt','w')
with urllib.request.urlopen(url) as f:
    obj = pickle.load(f)
    for pairs in obj:
        f2.write(''.join([pair[0]*pair[1] for pair in pairs]))
        f2.write('\n')

