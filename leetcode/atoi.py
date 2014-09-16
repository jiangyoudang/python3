import time


def atoi(str):
    string = str.lstrip()
    if not string:
        return 0
    if string[0] in '-+0123456789':
        for i in range(1,len(string)):
            if string[i] not in '0123456789':
                string = string[:i]
                break

    try:
        res = int(string)
        if res>=2147483647:
            return 2147483647
        elif res<=-2147483648:
            return -2147483648
        else:
            return res
    except:
        return 0

t1 = time.time()
print(atoi('1'))
t2 = time.time()
print(t2-t1)