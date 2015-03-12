#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        middle = head
        end = head
        while end and end.next:
            middle = middle.next
            end = end.next.next

        # reverse nodes after middle
        if not middle or not middle.next:
            return head
        p = middle.next
        temp = None
        while p:
            pnext = p.next
            p.next = temp
            temp = p
            p = pnext
        middle.next = temp


        #insert
        p = head
        while middle.next:
            curr = middle.next
            middle.next = curr.next
            curr.next = p.next
            p.next = curr
            p = p.next.next
        return head
