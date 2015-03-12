# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        p = head
        pre_head = ListNode(0)
        pre_head.next = head
        pre = pre_head
        while p and p.next:
            pre.next = p.next
            pnext = p.next.next
            p.next.next = p
            p.next = pnext
            pre = p
            p = pnext

        return pre_head.next