from random import randint

filename = 'CL.txt'

with open(filename,'w') as f:
    for i in range(3000):
        c = chr(randint(32,126))
        f.write(c)
        if i%2:
            f.write('\n')
