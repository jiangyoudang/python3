'''
 if i > j and A[i] > A[j], then it is surpasser
'''
# merge sort
# return number of surpasser of each element
def merge(list_l, list_r, res):
    '''

    :param list_l: left partition
    :param list_r: right partition
    :param res: res dict
    :return:
    '''
    list_res = []
    n = len(list_l)
    i, j = 0, 0
    while i < len(list_l) and j < len(list_r):
        if list_l[i] < list_r[j]:
            list_res.append(list_l[i])
            res[list_l[i]] += len(list_r) - j
            i += 1
        else:
            list_res.append(list_r[j])
            j += 1
    while i < len(list_l):
        list_res.append(list_l[i])
        i += 1
    while j < len(list_r):
        list_res.append(list_r[j])
        j += 1

    return list_res

def merge_sort(A, res):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid], res)
    right = merge_sort(A[mid:], res)
    return merge(left, right, res)


A = [i for i in range(10)]
from random import shuffle
shuffle(A)
res = {i:0 for i in A}
merge_sort(A, res)
print(A)
print(res)