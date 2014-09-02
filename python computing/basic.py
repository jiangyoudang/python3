__author__ = 'congliu'

'''   case 5
    class   '''
class Retangle:
    def __init__(self, xcood, ycood):
        self.x = xcood
        self.y = ycood

    def setsize(self,xcood, ycood):
        self.x = xcood
        self.y = ycood


r1 = Retangle(4,5)
r1.setsize(5,6)
print(r1.x)


'''case 4
    file    '''

# file = open('test.txt')
#
# for line in file:
#     print(line, end='')
# file.close()


'''case 3
    format    '''

# def growthrates(n):
#     'print in fancier type'
#     print(' i  i**2  i**3  2**i')
#     format_str = '{0:2d}{1:6d}{2:6d}{3:6d}'
#     for i in range(2,n+1):
#         print(format_str.format(i,i**2,i**3,2**i))
#
# growthrates(4)


'''case 2

    # eval() and *   '''
# def f(a):
#     'return average'
#     return sum(a)/len(a)
#
# # data = eval(input('Your data: '))
# # print(f(data))
#

'''case 1
   #'format in dict' **   '''

# di = dict(
# first = 'John',
# last = 'Doe',
# street = 'Main Street',
# number = 123,
# city = 'AnyCity',
# state = 'As',
# zipcode = '09867')
#
# print('{first} {last} \n{number} {street}\n{city}, {state} {zipcode}'.format(**di))