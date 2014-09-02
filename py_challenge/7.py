__author__ = 'congliu'

import urllib.request
from PIL import Image


url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
f = urllib.request.urlopen(url)
with open('7.png','wb') as my_image:
    my_image.write(f.read())
image = Image.open('7.png')
pix = image.load()
c = []
print('Image info:')
print(image.size,image.mode)
print('pix info:')
for j in range(image.size[1]-1):
    r = 0
    for i in range(image.size[0]):
        if pix[i,j] == pix[i,j+1]:
            r+=1
    c.append(r)
result = []
for i in range(0,608,7):
    result.append(pix[i,43][1])
for i in result:
    print(''.join(chr(i)),end='')
for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
    print(''.join(chr(i)),end='')



#for i in c:
#    print(chr(i),end=' ')
