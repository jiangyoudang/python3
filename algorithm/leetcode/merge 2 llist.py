# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        p1 = l1
        p2 = l2
        if l1.val <=l2.val:
            head = l1
            p1 = l1.next
        else:
            head = l2
            p2 = l2.next
        p = head
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        else:
            p.next = p2

        return head
