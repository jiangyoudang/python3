'''
Q1: S = power(2, p) * power(3, q);

A[0] = 1;
A[1] = 2;
A[2] = 3;
A[3] = 4;
A[4] = 6;
A[5] = 8;
A[6] = 9;
A[7] = 12;

求 A[N] , N >=0  && N <=200 in case of overflow

'''

def find_nth(n):
    if n == 0:
        return 1
    A = [1] * n
    j = 1
    k = 0
    for i in range(1, n):
        if A[k] * 2 < 3 ** j:
            A[i] = A[k] * 2
            k += 1
        else:
            A[i] = 3 ** j
            j += 1

    return A


print(find_nth(10))


'''
A sequence of numbers is called a zig-zag sequence if the differences
between successive numbers strictly alternate between positive and negative.'''

def find_lsubseq(seq):
    if not seq:
        return 0
    if len(seq) == 1:
        return 1
    count = int(seq[0] != seq[1]) + int(seq[-1] != seq[-2])


    equal_handle = 0
    # if seq[0] != seq[1]:
    #     equal_handle = 2 * int(seq[0] < seq[1]) - 1

    res = []
    if seq[0] != seq[1]:
        res.append(seq[0])

    for i in range(1, len(seq)-1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            count += 1
            res.append(seq[i])
        if seq[i] < seq[i-1] and seq[i] < seq[i+1]:
            count += 1
            res.append(seq[i])
        if seq[i] != seq[i-1] and seq[i] == seq[i+1]:
            equal_handle = int(seq[i] > seq[i-1]) * 2 - 1
            count += 1
            res.append(seq[i])
        elif seq[i] == seq[i-1] and seq[i] != seq[i+1]:
            if equal_handle == 0:
                res.append(seq[i])
            else:
                is_curr =  int(equal_handle != int(seq[i] < seq[i+1]) * 2 - 1)

                if not is_curr:
                    count -= 1
                    res.pop()
    if seq[-1] != seq[-2]:
        res.append(seq[-1])
    if count==0:
        count += 1
        res.append(seq[0])
    return (res, count)

# seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# seq = [ 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]
seq = [ 5,5,5,5,5, 6,5,6,5,7,8, 6,6 ,6, 6,6,6,6,6,6,6,6,6]
print(find_lsubseq(seq))

