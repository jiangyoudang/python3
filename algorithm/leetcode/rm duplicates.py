# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        p = head
        pre = head
        while p:
            if p.val == pre.val:
                pre.next = p.next
            else:
                pre = p
            p = p.next
        return head
