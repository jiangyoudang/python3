def minus(f):
    def a(*args):
        return 'c'+f(*args)
    return a

@minus
def xxx(x):
    print('ok')
    return 'b'+ x



def a(l=[1]):
    print(l)
    l.append(1)

a()
a()
