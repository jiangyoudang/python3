__author__ = 'congliu'

import re

with open('3.txt','r') as file1:
    content = file1.read().replace('\n','')

    result = re.findall(r'[^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+', content)
    for r in result:
        for r2 in re.findall('[A-Z][a-z][A-Z]',r):
            print(r2[1], end='')






        #line1 = file1.readline()
        #print(2340%len(line1))
        #content = file1.read()
        ##print(re.match('.*[a-zA-Z]', content).groups())
        #for m in re.finditer('[a-zA-Z]', content):
        #    print(m.start(),m.group())
        #print(''.join(re.findall('[a-zA-Z]', content)))

