# -*- coding utf-8 -*-
__author__ = 'congliu'


from random import randint

a = [randint(1,100) for i in range(50)]


def sift_down(a, start, end):
    root = start
    while True:
        child = 2*root + 1
        if child > end:
            break
        if child+1 <=end and a[child] < a[child+1]:
            child = child+1
        if a[root] < a[child]:
            a[root],a[child] = a[child], a[root]
            root = child
        else:
            break

def heapify(a):
    for start in range((len(a)-2)//2,-1,-1):
        sift_down(a,start,len(a)-1)

def heap_sort(a):
    heapify(a)
    for end in range(len(a)-1,0,-1):
        a[0],a[end] = a[end],a[0]
        sift_down(a,0,end-1)
    return a

print(heap_sort(a))