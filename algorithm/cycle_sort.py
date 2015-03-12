
l = [1,3,2,0,4,6,5]

def cyclesort_simple(l):
    # last_value = 0
    for i in range(len(l)):
        if i != l[i]:
            n = i
            while 1:
                tmp = l[n]
                if n != i:
                    l[n] = last_value
                last_value = tmp
                n = last_value
                if n == i:
                    l[n] = last_value
                    break


def cycle_sort(l):
    for i in range(len(l)):
        if i != l[i]:
            n = l[i]
            while n != i:
                tmp = l[n]
                l[n] = n
                n = tmp
            l[i] = n


cycle_sort(l)
# cyclesort_simple(l)

print(l)