# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        pre_head = ListNode(0)
        pre_head.next = head
        p = head
        while p.next:
            curr = p.next
            pre = pre_head
            if p.val <= curr.val:
                p = p.next
                continue
            while pre.next.val <= curr.val:
                pre = pre.next
        
            
            p.next = curr.next
            curr.next = pre.next
            pre.next = curr
                
        return pre_head.next
            