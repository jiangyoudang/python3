__author__ = 'congliu'

# good code

#1  if symbol in '([{':
#2  for i in [c for c in coin if c <= change]    // comprehensive
#3  multiple = 1024 if False else 1000

#4
#import re
#def remove_tags(s):
#    result = re.sub(r'<.*?>',' ',s)
#    return result.split()

#5
#pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]
#pairs.sort(key=lambda pair:pair[1])
#or ---key = str.lower

#6

    #for i in obj:
        #print(''.join(map(lambda i_tuple: i_tuple[0]*i_tuple[1],i)))

    #print(''.join([i_tuple[0]*i_tuple[1] for i_tuple in obj]))

###  Generally the 2 ways are equal. Obviously, 2nd is better


#7

#def sequentialSearch(alist, item):
#    pos = 0
#    found = False
#    while pos < len(alist) and not found:
#        if alist[pos] == item:
#            found = True
#        else:
#            pos = pos+1
#
#    return found