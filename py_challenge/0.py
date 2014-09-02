__author__ = 'congliu'

import string

#print(type(string.ascii_lowercase))
toList = string.ascii_lowercase[2:]+'ab'
#toList = [chr(ord(a)+2) for a in string.ascii_lowercase[:-2]] + ['a','b']

#dict = {a:b for a in string.ascii_lowercase for b in toList}
dict = dict(zip(string.ascii_lowercase, toList))
table1 = str.maketrans(dict)
#table1 = str.maketrans(string.ascii_lowercase, toList)



text = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb \
       rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

print(text.translate(table1))

#[chr(ord(a)+2) for a in string.ascii_lowercase[:-2]]
