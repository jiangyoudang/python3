__author__ = 'congliu'


import random

#print(sum(2*x*y for x,y in itertools.combinations(range(1,101),2)))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def partion(head):
    if not head:
        return None
    if not head.next:
        return head
    middle, end = head, head
    pre = head
    while end and end.next:
        pre = middle
        middle = middle.next
        end = end.next.next
    pre.next = None

    link1 = partion(head)
    link2 = partion(middle)
    return merge(link1,link2)


def merge(link1, link2):
    p1 = link1
    p2 = link2
    if p1.val > p2.val:
        head = p2
        p2 = p2.next
    else:
        head = p1
        p1 = p1.next
    t = head
    while True:
        if not p1:
            t.next = p2
            break
        elif not p2:
            t.next = p1
            break
        if p1.val > p2.val:
            #p2,p2.next = p2.next, p1
            t.next = p2
            t = p2
            p2 = p2.next
        else:
            t.next = p1
            t = p1
            p1 = p1.next
    return head



def buildLinkedList():
    head = ListNode(random.randint(1,100))
    p1 = head
    for i in range(11):
        p2 = ListNode(random.randint(1,100))
        p1.next = p2
        p1 = p2
    return head

#head = buildLinkedList()

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(1)

#l = head
l = partion(head)

while l:
    print(l.val, end=' ')
    l = l.next