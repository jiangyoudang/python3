__author__ = 'congliu'

import zipfile,re
import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
f = urllib.request.urlopen(url)
with open('channel.zip','wb') as zipfile_write:
    zipfile_write.write(f.read())
zipfile1 = zipfile.ZipFile('channel.zip')
comment = []
#context = zipfile1.open('90052.txt').read().decode()
context = zipfile1.read('90052.txt').decode()
while True:

    nothing = re.findall(r'\d+',context)
    if not nothing:
        break
    comment.append(zipfile1.getinfo(''.join(nothing)+'.txt').comment.decode())
    context = zipfile1.open(''.join(nothing)+'.txt').read().decode()
    print(context)
print(''.join(comment))
#print(zipfile1.open('90052.txt').read().decode())
#for file_in_zip in zipfile1.infolist():
#    print(file_in_zip.filename,file_in_zip.comment)